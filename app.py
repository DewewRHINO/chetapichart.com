from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/blog")
def blog_page():
    return render_template('blog.html')