from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@password/Swm'
db = SQLAlchemy(app)


class Employee(db.Model):
    '''
    id, name phone_num, msg, date, email
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/signin", methods = ['GET', 'POST'])
def signin():
    if(request.method=='POST'):
        '''Add entry to the database'''
        username = request.form.get('username')
        password = request.form.get('password')
        check = Employee.query.filter_by(username=username).first()
        
        if check.password == password:       
            return render_template('index.html')

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        entry = Employee(name=name, username=username,password=password, date= datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('product.html')

# @app.route("/emp", methods = ['GET', 'POST'])
# def contact():
#     if(request.method=='POST'):
#         '''Add entry to the database'''
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         message = request.form.get('message')
#         entry = empolyee(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
#         db.session.add(entry)
#         db.session.commit()
#     return render_template('contact.html')

app.run(debug=True)


