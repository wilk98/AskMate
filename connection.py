import csv
from datetime import datetime
import time
from operator import itemgetter


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


def delete_question(question_id):
    with open('question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        questions_list = []
        for item in reader:
            if item['id'] != question_id:
                questions_list.append(item)
    with open('question.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, QUESTION_HEADER)
        writer.writeheader()
        writer.writerows(questions_list)


def delete_answer(question_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        answers_list = []
        for item in reader:
            if item['question_id'] != question_id:
                answers_list.append(item)
    with open('answer.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, ANSWER_HEADER)
        writer.writeheader()
        writer.writerows(answers_list)

def delete_answer_one(answer_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        answers_list = []
        for item in reader:
            if item['id'] != answer_id:
                answers_list.append(item)
    with open('answer.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, ANSWER_HEADER)
        writer.writeheader()
        writer.writerows(answers_list)


def get_answer(question_id):
    answers = []
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            if question_id == item['question_id']:
                answers.append(item)
    return answers

def get_answer_one(answer_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            if answer_id == item['id']:
                ts_epoch = int(item['submission_time'])
                item['submission_time'] = datetime.fromtimestamp(ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
                return item



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


def vote_question_up(question_id):
    with open('question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        questions_list = []
        for item in reader:
            if int(item['id']) == int(question_id):
                number = int(item['vote_number'])
                number += 1
                item['vote_number'] = number
            questions_list.append(item)
    with open('question.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, QUESTION_HEADER)
        writer.writeheader()
        writer.writerows(questions_list)


def vote_question_down(question_id):
    with open('question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        questions_list = []
        for item in reader:
            if int(item['id']) == int(question_id):
                number = int(item['vote_number'])
                number -= 1
                item['vote_number'] = number
            questions_list.append(item)
    with open('question.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, QUESTION_HEADER)
        writer.writeheader()
        writer.writerows(questions_list)


def vote_answer_up(answer_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        answer_list = []
        for item in reader:
            if int(item['id']) == int(answer_id):
                number = int(item['vote_number'])
                number += 1
                item['vote_number'] = number
            answer_list.append(item)
    with open('answer.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, ANSWER_HEADER)
        writer.writeheader()
        writer.writerows(answer_list)


def vote_answer_down(answer_id):
    with open('answer.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        answer_list = []
        for item in reader:
            if int(item['id']) == int(answer_id):
                number = int(item['vote_number'])
                number -= 1
                item['vote_number'] = number
            answer_list.append(item)
    with open('answer.csv', 'w', newline='') as writeFile:
        writer = csv.DictWriter(writeFile, ANSWER_HEADER)
        writer.writeheader()
        writer.writerows(answer_list)

def top_questions():
    all_questions = []
    with open('question.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            all_questions.append(item)
    return sorted(all_questions, key=itemgetter('view_number'), reverse=True)
