from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlachemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "6358c61aaba8619f201e9b2772c66d75"
db = SQLAlchemy(app)


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.String(20), unique=True, nullable =False)
    email = db.column(db.String(120), unique=True, nullable =False)
    image_file = db.column(db.String(20), nullable =False, default= "default.jpg")
    password = db.Column(db.String(60),nullable = False)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Posts(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    

posts = [
    {
        "author": "Kiprotich",
        "title": "First Blog post",
        "content": "My first content",
        "date_posted": "April 20, 2019"
    },
    {
        "author": "Kiprotich Dominic",
        "title": "First Blog post",
        "content": "My first content",
        "date_posted": "April 20, 2020"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    title = "About page"
    return render_template("about.html", title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f"Account created successfully for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in", "success")
            return redirect(url_for("home"))
        else:
            flash("Log In Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title=LoginForm, form=form)


if __name__ == "__main__":
    app.run(debug=True)
