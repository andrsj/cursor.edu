from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    last = db.Column(db.String(20), nullable = False)
    kurs = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return 'Student: {} {}'.format(self.name, self.last)


@app.route('/')
def index():
    return render_template('index.html')