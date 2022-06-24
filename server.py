from flask import Flask, render_template, request, redirect
import time
import connection
import csv

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html')


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
    answers_to_show = connection.get_answer(question_id)
    if answers_to_show != None:
        return render_template('question_to_show.html', question_id=question_id,
                               submission_time=question_to_show.get('submission_time'),
                               view_number=question_to_show.get('view_number'),
                               vote_number=question_to_show.get('vote_number'),
                               title=question_to_show.get('title'),
                               message=question_to_show.get('message'),
                               image=question_to_show.get('image'),
                               answer=answers_to_show,
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


@app.route("/answer/<answer_id>")
def display_answer(answer_id):
    answer_to_show = connection.get_answer_one(answer_id)
    return render_template('answer_to_show.html', answer_id=answer_id,
                               submission_time=answer_to_show.get('submission_time'),
                               vote_number=answer_to_show.get('vote_number'),
                               question_id=answer_to_show.get('question_id'),
                               message=answer_to_show.get('message'),
                               image=answer_to_show.get('image'),
                               )

@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    connection.delete_question(question_id)
    connection.delete_answer(question_id)
    return redirect('/list')


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
        return render_template('question.html', title=question_to_add.get('title'),
                               message=question_to_add.get('message'))


@app.route('/question/<question_id>/vote-up')
def que_vote_up(question_id):
    connection.vote_question_up(question_id)
    return redirect('/list')

@app.route('/question/<question_id>/vote-down')
def que_vote_down(question_id):
    connection.vote_question_down(question_id)
    return redirect('/list')

@app.route('/answer/<answer_id>/vote-up')
def ans_vote_up(answer_id):
    connection.vote_answer_up(answer_id)
    return redirect('/list')

@app.route('/answer/<answer_id>/vote-down')
def ans_vote_down(answer_id):
    connection.vote_answer_down(answer_id)
    return redirect('/list')

@app.route("/team")
def team_site():
    return render_template('team.html')


@app.route("/index")
def home_site():
    return render_template('index.html')


@app.route("/most_popular")
def most_popular_site():
    top_questions = connection.top_questions()
    return render_template('most_popular.html', most_popular=top_questions)




if __name__ == "__main__":
    app.run(debug=True)