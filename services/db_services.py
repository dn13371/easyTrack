from db import db, User, Project
from faker import Faker


def create(db):   
    db.create_all()
    

def populate(db):
    fake = Faker()
    for _ in range(10):  
        user = User(
            mail=fake.email(),
            username=fake.user_name(),
            password="password",  
        )
        project = Project(
            userID = 11, 
            projectName = fake.city(),
            projectStatus = 1,
        )
        db.session.add(user)
        db.session.add(project)
    db.session.commit()
