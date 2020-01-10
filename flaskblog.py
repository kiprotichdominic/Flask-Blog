from flask import Flask, render_template, url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "e4f5574dafdc479321bb1c66c18147f577f3f452"

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
    return render_template("index.html", posts=posts, title="Home page")


@app.route("/about")
def about():
    return render_template("about.html", title = "About")


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login", form=form)


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", form = form, title = "Register")


if __name__ == "__main__":
    flaskblog.run(debug=True)
