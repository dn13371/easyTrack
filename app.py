from flask import Flask, render_template, request, jsonify, flash, session, redirect, url_for
from db import db, User, Project, Timestamp
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
    projects = Project.query.filter_by(userID = user_id, projectStatus = 1).all()

    return render_template('dashboard.html', projects = projects)

#project page

@app.route('/project/<int:project_id>', methods = ['GET', 'POST'])
@login_required
def project(project_id):
    if request.method == 'GET':
        user_id = current_user.id
        access = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            runningTimestamp = Timestamp.query.filter_by(projectID = project_id, endTime = None).first()
            if runningTimestamp: 
                running = 1
                now = datetime.datetime.now()
                diff = now - runningTimestamp.startTime
                timediff = int(diff.total_seconds() * 1000)  


            else:
                running = 0 
                timediff = 0   
            return render_template('project.html', project = access, running  = running, milliseconds = timediff)
          #  return render_template('project.html', project_name = access.projectName, project_id = access.id)
    
        else: 
            return 'no access'

    else: 
        return'invalid action'

#timer control routes
@app.route('/start/<int:project_id>', methods = ['POST'])
@login_required
def startTime(project_id):
    if request.method == 'POST':
        user_id = current_user.id
        access = Project.query.filter_by(userID =user_id, id = project_id).first()
        if access: 
            timestamp = Timestamp(projectID=project_id,startTime = datetime.datetime.now(), endTime = None)
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
        access = Project.query.filter_by(userID =user_id, id = project_id).first()
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
        access = Project.query.filter_by(userID =user_id, id = project_id).first()
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