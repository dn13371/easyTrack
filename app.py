from flask import Flask, render_template, request
import click

app = Flask(__name__)

# Load configuration from a separate file or from app.py itself
app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    SQLALCHEMY_DATABASE_URI='sqlite:///todos.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


@app.route('/index')
def index():

    return 'penis'



if __name__ == '__main__':
    app.run(debug=True)
