from flask import Flask, render_template, request, url_for, redirect
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.txt",
)

logger = logging.getLogger("flask_app")
# Always create flask object with different name so we are using __name__ bcoz for every file it will be different


app = Flask(__name__)
posts = {
    0: {
        "title": "Hello, World",
        "content": "This is my first blog post",
    },
}


@app.route("/")  # /
def home():
    return render_template("home.jinja2", posts = posts)


@app.route("/post/<int:post_id>")  # /post/0, 0 -> post_id
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template(
            "404.jinja2", message=f"A post with id {post_id} was not found"
        )
    return render_template("post.jinja2", post=post)


@app.route("/post/create", methods=["GET", "POST"])
def create_post():
    # Trough this method we are sending all the data through url which is not secure as someone can see it once he can intercept the requests another methods is to request.form ?title=..... aab payload se hoga
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        index = len(posts)
        posts[index] = {"title": title, "content": content}
        return redirect(url_for("post", post_id=index))
    return render_template("create_form.jinja2")


if __name__ == "__main__":
    app.run(debug=True)
