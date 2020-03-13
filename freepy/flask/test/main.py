from flask import Flask, render_template, request, redirect, url_for
from config import DEGUB
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = DEGUB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stud.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    last = db.Column(db.String(20), nullable = False)
    kurs = db.Column(db.Integer, nullable = False, default = 1)

    def __repr__(self):
        return "Student by id {}".format(self.id)

# >>> form main import db, Student
# >>> db.create_all()
# >>> Student.query.all()
# []
# >>> db.session.add(Student(name = "Andrew", last = "Derkach", kurs = 3) )
# >>> Student.query.all()
# [Student by id 1]
# >>> Student.query.all()[0]
# Student by id 1
# >>> Student.query.all()[0].name
# Andrew

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hi, %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/html/')
@app.route('/html/<name>')
def show_html(name = None):
    return render_template('index.html', name = name)


@app.route('/form', methods=['GET', 'POST'])
def form_html():
    if request.method == 'POST':
        name = request.form['name']
        last = request.form['last']
        kurs = request.form['kurs']
        new_student = Student(name = name, last = last, kurs = kurs)
        db.session.add(new_student)
        db.session.commit()
        return redirect('/form')
    else:
        students = Student.query.order_by(Student.name).all()
        return render_template('form.html', students=students)

@app.route('/form/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/form')

if __name__ == "__main__":
    app.run()