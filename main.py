from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", blog=blog_url)


@app.route('/post/<blog_num>')
def post(blog_num):
    blog_url = (requests.get("https://api.npoint.io/c790b4d5cab58020d391")).json()
    return render_template("post.html", blog=blog_url, id=int(blog_num))


if __name__ == "__main__":
    app.run(debug=True)
