from flask import Flask, Markup, render_template, request, redirect, url_for, make_response
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Dev = False
Prod = True

# dev database string
if Dev:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

# production database string
if Prod:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Zivish2019#@localhost/hela"

UPLOAD_FOLDER = 'static/uploads'
app.config['login_template'] = "/auth/login.html"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SQLALCHEMY_ECHO'] = True

# Live
os.environ['EMAIL_USER'] = 'info@mwarangu.com'
os.environ['EMAIL_PASSWORD'] = ''

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
# mail = Mail(app)

app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Your Financial Expenditure', max=17000, set=zip(values, labels, colors))

db.create_all()
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5050)