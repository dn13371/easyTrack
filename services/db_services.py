from db import db, User 
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
        db.session.add(user)
    db.session.commit()
