import csv
from datetime import datetime
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
        for item in reader:
            last_id = int(item['id'])+1
        answer['id'] = last_id
        answer['submission_time'] = int(time.time())
        writer = csv.DictWriter(csvfile, ANSWER_HEADER)
        writer.writerow(answer)


def post_question(question):
    with open('question.csv', 'r+', newline='') as csvfile:
        last_id = 1
        reader = csv.DictReader(csvfile)
        for item in reader:
            last_id = int(item['id']) + 1
        question['id'] = last_id
        question['submission_time'] = int(time.time())
        writer = csv.DictWriter(csvfile, QUESTION_HEADER)
        writer.writerow(question)