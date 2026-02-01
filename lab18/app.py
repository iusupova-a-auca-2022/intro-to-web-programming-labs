from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
# Becomes the view function for root URL,
#     will execute this function to determine what to return when visits "/"
def index():
    names = ["Alice", "Charlie", "David"]
    return render_template("index.html", names=names, title="Welcome!")

@app.route('/greet/<name>')
def greet(name):
    return f"<h2>Hello, {escape(name.capitalize())}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)