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