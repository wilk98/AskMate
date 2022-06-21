from flask import Flask, render_template, request, redirect

import connection

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('base.html')


@app.route("/list")
def show_questions():
    questions = connection.read_questions()
    return render_template('list.html', questions=questions)


@app.route('/story', methods=['GET', 'POST'])
def add_user_story():
    answer_to_post = {}
    # when we submit the form with POST method we will have the string 'POST' in request.method
    if request.method == 'POST':
        # we save the new note we got from the POST values
        answer_to_post['id'] = 0
        answer_to_post['submission_time'] = request.form['submission_time']
        #answer_to_post['vote_number'] = #counter
        answer_to_post['question_id'] = 'question_id'
        answer_to_post['message'] = request.form['message']
        answer_to_post['image'] = request.form['image']
        # we update how many times it has been edited
        #saved_data['id'] = saved_data.get('id', 0) + 1
        connection.post_answer('question_id')
        return redirect('/list')
    #if the method is GET, show the stories page
    # return render_template('story.html', story_title=saved_story.get('story_title'),
    #                        user_story=saved_story.get('user_story'),
    #                        acceptance_criteria=saved_story.get('acceptance_criteria'),
    #                        business_value=saved_story.get('business_value'),
    #                        estimation=saved_story.get('estimation'))


@app.route("/question/<question_id>/new_answer")
def route_new_answer(answer):
    return render_template("answer.html")


if __name__ == "__main__":
    app.run()
