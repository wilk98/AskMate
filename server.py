from flask import Flask, render_template, request, redirect
import connection
<<<<<<< HEAD
import data_manager
=======
>>>>>>> 9af9a629b3441288aaedf0ea927c293bfd047fa8
from datetime import datetime

import data_manager

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html')


@app.route("/list")
def show_questions():
    order_by_column = request.args.get('column-select')
    dir = request.args.get('order')
    if order_by_column:
        questions = data_manager.get_question_by_column(order_by_column, dir)
    else:
        questions = data_manager.read_questions()
    return render_template('list.html', list=questions, column_select=order_by_column, order=dir)


@app.route('/question', methods=["POST", "GET"])
def add_question():
    ts_epoch = (int(time.time()))
    question_to_add = {}
    if request.method == "POST":
        question_to_add['submission_time'] = str(datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S'))
        question_to_add['view_number'] = 0
        question_to_add['vote_number'] = 0
        question_to_add['title'] = request.form['title']
        question_to_add['message'] = request.form['message']
        question_to_add['image'] = request.form['image']
        data_manager.post_question(question_to_add)
        return redirect('/list')
    else:
        return render_template('question.html', title=question_to_add.get('title'),
                               message=question_to_add.get('message'))


@app.route('/question/<question_id>/new_answer', methods=['POST', 'GET'])
def add_new_answer(question_id):
    ts_epoch = (int(time.time()))
    answer_to_post = {}
    if request.method == 'POST':
        answer_to_post['submission_time'] = str(datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S'))
        answer_to_post['vote_number'] = 0
        answer_to_post['question_id'] = question_id
        answer_to_post['message'] = request.form['message']
        answer_to_post['image'] = request.form['image']
        data_manager.post_answer(answer_to_post)
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
    question_to_show = data_manager.get_question(question_id)
    answers_to_show = data_manager.get_answers(question_id)
    tag_id = data_manager.get_tag_id(question_id)
    tag_list = [row["tag_id"] for row in tag_id]
    tags_to_show = []
    for i in tag_list:
        tag_to_show = data_manager.get_tag(i)
        tags_list = [row["name"] for row in tag_to_show]
        tags_to_show.append(tags_list[0])
    all_tags=[]
    for i in tags_to_show:
        if i[0] != "#":
            i = "#" + i
            all_tags.append(i)
        else:
            all_tags.append(i)
    return render_template('question_to_show.html', question=question_to_show[0], answers=answers_to_show, tag=all_tags)


@app.route("/answer/<answer_id>")
def display_answer(answer_id):
    answer_to_show = data_manager.get_answer(answer_id)
    return render_template('answer_to_show.html', answer=answer_to_show[0])


@app.route('/question/<question_id>/delete')
def delete_question(question_id):
    print(question_id)
    data_manager.delete_answers(question_id)
    data_manager.delete_question(question_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/delete')
def delete_answer(answer_id):
    data_manager.delete_answer(answer_id)
    return redirect('/list')


@app.route('/question/<question_id>/vote-up')
def que_vote_up(question_id):
    data_manager.vote_question_up(question_id)
    return redirect('/list')


@app.route('/question/<question_id>/vote-down')
def que_vote_down(question_id):
    data_manager.vote_question_down(question_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/vote-up')
def ans_vote_up(answer_id):
    data_manager.vote_answer_up(answer_id)
    return redirect('/list')


@app.route('/answer/<answer_id>/vote-down')
def ans_vote_down(answer_id):
    data_manager.vote_answer_down(answer_id)
    return redirect('/list')


<<<<<<< HEAD
@app.route('/question/<question_id>/edit', methods=["POST", 'GET'])
def edit_question(question_id):
    question_to_edit = {}
    if request.method == "POST":
        question_to_edit['id'] = question_id
        question_to_edit['title'] = request.form['title']
        question_to_edit['message'] = request.form['message']
        question_to_edit['image'] = request.form['image']
        data_manager.edit_question(question_to_edit)
        return redirect(f'/question/{question_id}')
    else:
        return render_template('edit_question.html', question_id=question_id)


@app.route('/answer/<answer_id>/edit', methods=["POST", 'GET'])
def edit_answer(answer_id):
    answer_to_edit = {}
    if request.method == "POST":
        answer_to_edit['id'] = answer_id
        answer_to_edit['message'] = request.form['message']
        answer_to_edit['image'] = request.form['image']
        data_manager.edit_answer(answer_to_edit)
        return redirect(f'/answer/{answer_id}')
    else:
        return render_template('edit_answer.html', answer_id=answer_id)


@app.route("/question/<question_id>/new-tag", methods=["POST", 'GET'])
def add_tag(question_id):
    if request.method == "POST":
        new_tag = request.form['tag']
        data_manager.add_tag(new_tag)
        return redirect(f'/question/{question_id}')
    else:
        return render_template('tag.html')


=======
>>>>>>> 9af9a629b3441288aaedf0ea927c293bfd047fa8
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
