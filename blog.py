from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm           #importing regitration and login form that we created in forms.py
app = Flask(__name__)

app.config('SECRET_key') = '479d335f1db1939d9144f9f51450f75c'   #

Possts = [ #Possts is a variable, array conating two dictonary
    {
        'author': 'bjle',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2010'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")      #home and main root page conatain the same function home()
def home():
    return render_template('home.html', jai_posts=Possts) #jai_posts is a varible declared and is set to above used Possts array
#render templates ke liye tamplates folder me hona chaiye home.html

@app.route("/about")
def about():
    return render_template('about.html', title='About')  #as title is given here so it will displayed in place if flask blog

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register Yourself', foorm=form)

@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='Login Now', foorm=form)

if __name__ == '__main__':
    app.run(debug=True)          #used to update on refresh(debug mode ONN)
