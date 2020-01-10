from flask import Flask, render_template,url_for
app = Flask(__name__)

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
    return render_template("index.html", posts= posts,title = "Home page")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    flaskblog.run(debug=True)