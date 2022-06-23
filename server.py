from flask import Flask, render_template, request, redirect
import time
import connection
import csv

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('base.html')


@app.route("/list")
def show_questions():
    questions = connection.read_questions()
    return render_template('list.html', list=questions)


@app.route('/question/<question_id>/new_answer', methods=['GET', 'POST'])
def add_new_answer(question_id):
    answer_to_post = {}
    if request.method == 'POST':
        answer_to_post['id'] = 0
        answer_to_post['vote_number'] = 0
        answer_to_post['question_id'] = question_id
        answer_to_post['message'] = request.form['message']
        # answer_to_post['image'] = request.form['image']
        connection.post_answer(answer_to_post)
        return redirect('/list')
    return render_template('answer.html',
                           question_id=question_id,
                           message='')


# @app.route("/question/<question_id>")
# def route_new_answer(question_id):
#     answer_to_display = connection.get_answer(question_id)
#     return render_template("answer.html", answer_id=answer_to_display.get('id'),
#                            message=answer_to_display.get('message'))


@app.route('/question/<question_id>')
def display_question(question_id):
    question_to_show = connection.get_question(question_id)
    answer_to_show = connection.get_answer(question_id)
    if answer_to_show != None:
        return render_template('question_to_show.html', question_id=question_id,
                               submission_time=question_to_show.get('submission_time'),
                               view_number=question_to_show.get('view_number'),
                               vote_number=question_to_show.get('vote_number'),
                               title=question_to_show.get('title'),
                               message=question_to_show.get('message'),
                               image=question_to_show.get('image'),
                               answer=answer_to_show.get('message')
                               )
    else:
        return render_template('question_to_show.html', question_id=question_id,
                               submission_time=question_to_show.get('submission_time'),
                               view_number=question_to_show.get('view_number'),
                               vote_number=question_to_show.get('vote_number'),
                               title=question_to_show.get('title'),
                               message=question_to_show.get('message'),
                               image=question_to_show.get('image'),
                               answer= "No answer yet"
                               )


@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    connection.delete_question(question_id)
    return redirect('/')


@app.route('/question', methods=["POST", "GET"])
def add_question():
    question_to_add = {}
    if request.method == "POST":
        question_to_add['id'] = 0
        question_to_add['submission_time'] = int(time.time())
        question_to_add['view_number'] = 0
        question_to_add['vote_number'] = 0
        question_to_add['title'] = request.form["title"]
        question_to_add['message'] = request.form["message"]
        # question_to_add['image'] = request.form["image"]
        connection.post_question(question_to_add)
        return redirect('/')
    else:
        return render_template('question.html')


if __name__ == "__main__":
    app.run(debug=True)

