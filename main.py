from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post = Post()
    all_posts = post.get_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    post = Post()
    blog = post.get_post(blog_id)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
