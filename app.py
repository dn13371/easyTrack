from flask import Flask, render_template, request
from db import db
import click
from services import db_services
from config import DevConfig, TestConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)

#CLI commands
@app.cli.command('init-db')
def init_db(): 
    db_services.create(db)
    db_services.populate(db)

#Routes 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET': 
        return render_template('base.html')
    if request.method == 'POST'
        mail = request.form.get('email')
if __name__ == '__main__':
    app.run()