from flask import Flask, render_template, url_for, request
from forms import PostForm


app = Flask(__name__)

@app.route('/create')
def create_post():
    form = PostForm()
    return render_template('/create_post.html', form=form)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/list")
def list_page():
    return render_template('list.html')


@app.route('/question')
def questions_page():
    return render_template('question.html')


if __name__ == "__main__":
    app.run(debug=True)
