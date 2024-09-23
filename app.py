from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
from db import db, User, Project, Timestamp, Access
import click
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from services import db_services
from config import DevConfig, TestConfig
import datetime

app = Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

# flask login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#CLI commands
@app.cli.command('init-db')
def init_db(): 
    db_services.create(db)
    db_services.populate(db)
@app.cli.command('drop-db')
def drop_db(): 
    db.drop_all()

#Routes 

#register 
@app.route('/register', methods = ['GET', 'POST'])
def register(): 
    if request.method == 'GET': 
       return render_template('register.html')

    if request.method == 'POST': 
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
                                
        if User.query.filter_by(mail = email).first(): 
            flash('email already registered')
            return redirect(url_for('register'))
    
    new_user = User(mail=email, username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    
    flash('suckess')
    return redirect(url_for('login'))

#login
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET': 
        return render_template('base.html')
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(mail=mail).first()

        if user and user.check_password(password): 
            login_user(user)
            return redirect(url_for('dashboard'))
        
        else: 
            flash('wrong email')
            return redirect(url_for('login'))

#logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))




#lockedcontent only for logged in users
@app.route('/dashboard')
@login_required
def dashboard(): 
    user_id = current_user.id
    accessible_projects = Access.query.with_entities(Access.projectID).filter_by(userID=user_id).all()
    project_ids = [project_id[0] for project_id in accessible_projects]
    projects2 = Project.query.filter_by(userID = user_id, projectStatus = 1).all()
    projects = Project.query.filter(
    Project.userID == user_id,
    Project.projectStatus == 1,
    Project.id.in_(project_ids)
    ).all()
    return render_template('dashboard.html', projects = projects)

#project page

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@login_required
def project(project_id):
    if request.method == 'GET':
        user_id = current_user.id
        access = Access.query.filter_by(userID =user_id, projectID = project_id).first()
        if access: 
            project = Project.query.filter_by(userID =user_id, id = project_id).first()

            runningTimestamp = Timestamp.query.filter_by(projectID = project_id, endTime = None).first()
            if runningTimestamp: 
                running = 1
                now = datetime.datetime.now()
                diff = now - runningTimestamp.startTime
                timediff = int(diff.total_seconds() * 1000)  


            else:
                running = 0 
                timediff = 0   
            return render_template('project.html', project = project, running  = running, milliseconds = timediff)
          #  return render_template('project.html', project_name = access.projectName, project_id = access.id)
    
        else: 
            return 'no access'

    else: 
        return'invalid action'

#timer control routes
@app.route('/start', methods = ['POST'])
@login_required
def startTime():
    if request.method == 'POST':
        data=request.get_json()
        project_id = data.get('projectID')
        tag_content = data.get('tagContent')
        print(tag_content)
        user_id = current_user.id
        access = Access.query.filter_by(userID =user_id, projectID = project_id).first()

        owner = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            timestamp = Timestamp(projectID=project_id,startTime = datetime.datetime.now(), endTime = None, activity = tag_content)
            db.session.add(timestamp)
            db.session.commit()
            return jsonify({'success': True}) 

            
        else: 
            return jsonify({'success': False}), 403 
        
@app.route('/stop/<int:project_id>', methods = ['POST'])
@login_required
def stopTime(project_id):
    if request.method == 'POST':
        user_id = current_user.id
        access = Access.query.filter_by(userID =user_id, projectID = project_id).first()

        owner = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            ##see if there is a timer already running (only starttime, no endtime)
            currentTimestamp = Timestamp.query.filter_by(projectID = project_id, endTime = None).first()
            if currentTimestamp: 
                currentTimestamp.endTime = datetime.datetime.now()
                db.session.commit()
                return jsonify({'success': True}) 
            else: 
                return jsonify({'success': False}) , 403
        else: 
            return jsonify({'success': False}) , 403

##load all timestamps 
@app.route('/load/<int:project_id>', methods = ['POST'])
@login_required
def loadtimestamps(project_id):
    if request.method == 'POST': 
        user_id = current_user.id
        access = Access.query.filter_by(userID =user_id, projectID = project_id).first()

        owner = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            timestamps = Timestamp.query.filter(Timestamp.projectID == project_id, Timestamp.endTime != None).all()
            timestamps_list = []
            for timestamp in timestamps: 
                timestamps_list.append({
                    'id': timestamp.id, 
                    'tag': timestamp.activity, 
                    'start': timestamp.startTime.isoformat(),
                    'end': timestamp.endTime.isoformat()
                }
                )
                
            return jsonify({'timestamps': timestamps_list})
        else: 
            return jsonify({'success': False}) , 403
    else: 
        return jsonify({'success': False}) , 403

##create list of users with access to project

@app.route('/access/<int:project_id>', methods = ['POST'])
@login_required
def access(project_id):
    if request.method == 'POST': 
        user_id = current_user.id
        access = Access.query.filter_by(userID=user_id, projectID=project_id).first()
        owner = Project.query.filter_by(userID=user_id, id=project_id).first()

        if access or owner:  # Allow access if the user is a collaborator or the owner
            collaborators = Access.query.filter(Access.projectID == project_id).all()
            collaborator_list = []

            for collaborator in collaborators:
                user = User.query.filter_by(id=collaborator.userID).first()  # Correct query to fetch collaborator's info
                collaborator_list.append({
                    'userID': collaborator.userID,  # Correct to collaborator's userID
                    'userName': user.username,      # Get the collaborator's username
                })

            return jsonify({'collaborators': collaborator_list})  # Use 'collaborators' key
        else:
            return jsonify({'success': False}), 403
    else:         
        return jsonify({'success': False}), 403

##route to add access to a project 
@app.route('/gainaccess', methods = ['POST'])
@login_required 
def gainaccess(): 
    data = request.get_json()
    user_id = data.get('userID')
    projectID = data.get('projectID')
    print(user_id)
    print(projectID)
    access = Access.query.filter_by(userID = user_id, projectID = projectID).first()

    if access: 
        return jsonify({'success': False})
    else: 
        newAccess = Access(
            userID = user_id, 
            projectID = projectID
        )
        db.session.add(newAccess)
        db.session.commit()
        return jsonify({'success': True})
##route to revoke access to a project 
@app.route('/revokeaccess', methods = ['POST'])
@login_required 
def revokeaccess(): 
    data = request.get_json()
    user_id = data.get('userID')
    projectID = data.get('projectID')
    print(user_id)
    print(projectID)
    access = Access.query.filter_by(userID = user_id, projectID = projectID).first()
    project = Project.query.filter_by(id = projectID, userID = user_id ).first()

    if access: 
        if project == None: 
            db.session.delete(access)
            db.session.commit()
            return jsonify({'success': True})
        else: 
            return jsonify({'success': False})
    else: 
        return jsonify({'success': False})


##create new project 
@app.route('/create', methods = ['POST'])
@login_required
def create(): 
    data = request.get_json()
    projectName = data.get('projectName')
    print(projectName)
    user_id = current_user.id
    project = Project(
            userID = 11, 
            projectName = projectName, 
            projectStatus = 1,
    )

    db.session.add(project)
    db.session.commit()
    new_project_id = project.id
    access = Access(
            userID = user_id,
            projectID = new_project_id
        )   
    db.session.add(access)
    db.session.commit()
    return jsonify({'new_project_id': new_project_id}) 

##delete project 


if __name__ == '__main__':
    app.run()


"""@app.route('/pause/<int:project_id>', methods = ['POST'])
def pauseTime(project_id):
    if request.method == 'POST':
        user_id = current_user.id
        access = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            #if timestamp wasnt paused
            if not session.get('timestamp.Pause'): 
                session ['timestampPause'] = datetime.datetime.now()
            #if timestamp is paused
            if not session.get('timestamp.Pause'): 
                

        else: 
            return 'no access'     
"""