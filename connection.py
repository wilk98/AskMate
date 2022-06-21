import csv

QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image',]
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image',]


def read_questions():
    questions = []
    with open('question.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            questions.append(item)
    return questions


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

