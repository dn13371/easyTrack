from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)
 
class Project(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String, nullable=False)
    projectName = db.Column(db.String, nullable=False)
    #status 1 = current, status 2 = archived
    projectStatus = db.Column(db.String, nullable=False)

class Timestamp(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.String, nullable=False)
    activity = db.Column(db.String, nullable=False)
    startTime = db.Column(db.Time, nullable=False)
    endTime = db.Column(db.Time, nullable=False)
 