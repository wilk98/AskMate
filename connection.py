import csv
from datetime import datetime
from csv import writer
import time

QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


def read_questions():
    questions = []
    with open('question.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            ts_epoch = int(item['submission_time'])
            item['submission_time'] = datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
            questions.append(item)
    return sorted(questions, key=lambda item: item['submission_time'], reverse = True)


def get_question(question_id):
    with open('question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            if question_id == item['id']:
                question_to_display = item
        return question_to_display


def get_answer(question_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            if question_id == item['question_id']:
                answer_to_display = item
        return answer_to_display


def post_answer(answer):
    with open('answer.csv', 'r+', newline='') as csvfile:
        last_id = 1
        reader = csv.DictReader(csvfile)
        for answer in reader:
            last_id = int(answer['id'])+1
        answer['id'] = last_id
        #answer['submission_time'] = #z formularza
        answer['vote_number'] = 0
        answer['question_id'] = 'question_id'
        ##answer['message'] = #z formularza
        #answer['image'] = #z formularza
        writer = csv.DictWriter(csvfile, QUESTION_HEADER)
        writer.writerow(answer)

def post_question(title, question):
    rowcount = 0
    for row in open("question.csv"):
        rowcount += 1
    submission_time = int(time.time())
    new_file = [rowcount, submission_time, 0, 0, title, question, 'image']
    with open('question.csv', 'a', newline="") as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new_file)
        f_object.close()

# post_question("aaa", "ssasas")

