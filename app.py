from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired, Optional
from flask import render_template, redirect, request
from datetime import datetime
from flask_wtf import Form
from wtforms.fields.html5 import DateTimeField
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app1 = Flask(__name__)

app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app1.secret_key = 'SHH!'
db = SQLAlchemy(app1)  
Bootstrap(app1)
Moment(app1)


class AddTaskForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    company = StringField('Company')
    email = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    problem_desc=StringField('Problem Description', validators=[DataRequired()])
    date=DateTimeField(id='datepick', format='%m/%d/%Y %H:%M %p', validators=(validators.Optional(),))
    submit = SubmitField('Submit')




class CustomerPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, default='Unknown')
    phone_num = db.Column(db.String(20), nullable=True)
    company = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20), nullable=False, default='Unknown')
    subject = db.Column(db.String(20), nullable=False, default='Unknown')
    problem_description = db.Column(db.Text, nullable=False, default='Unknown')
    callback = db.Column(db.String(20), nullable=True)
    date_posted = db.Column(db.String(20), nullable=False,
                            default=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
    archive_flag = db.Column(db.String(10), nullable=False, default='0')                        
                            

    def __repr__(self):
        return 'CustomerPost' + str(self.id)


@app1.route('/')
def index():
    return render_template('index.html')


@app1.route('/administration')
def posts():
    all_posts = CustomerPost.query.filter_by(archive_flag=0).order_by(CustomerPost.date_posted).all()
    return render_template('administration.html', posts=all_posts)


@app1.route('/new_post', methods=['GET', 'POST'])
def newpost():
    form = AddTaskForm()
    if form.validate_on_submit():
        name=request.form['name']
        post_phone_num = request.form['phone_number']
        post_company = request.form['company']
        email=request.form['email']
        subject=request.form['subject']
        problem_desc = request.form['problem_desc']
        callback=request.form['date']
        new_post = CustomerPost(name=name, phone_num=post_phone_num, company=post_company, email=email,
                                subject=subject, problem_description=problem_desc, callback=callback, date_posted=datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
        
    else:
        return render_template('new_post.html', form=form)

@app1.route('/edit/<int:id>', methods = ['GET','POST'])
def edit(id):
    post = CustomerPost.query.get_or_404(id)
    if request.method == 'POST':
        post.name = request.form['name']
        post.phone_num = request.form['phone_num']
        post.company = request.form['company']
        post.email = request.form['email']
        post.subject = request.form['subject']
        post.problem_description = request.form['problem_description']
        post.callback = request.form['callback']
        db.session.commit()
        return redirect('/administration')
    else:
        return render_template('edit.html', posty = post)    
    
@app1.route('/hide/<int:id>', methods = ['GET','POST'])
def hide(id):
    post = CustomerPost.query.get_or_404(id)
    post.archive_flag = '1'
    db.session.commit()
    return redirect('/administration')
  
if __name__ == "__main__":
    app1.run(debug=True)    
