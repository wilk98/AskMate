from typing import List, Dict
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import db_common

@db_common.connection_handler
def read_questions(cursor):
    query = """
        SELECT *
        FROM question
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()

@db_common.connection_handler
def get_question(cursor, question_id):
    query = f"SELECT *  \
            FROM question\
            WHERE id = '{question_id}'"
    cursor.execute(query)
    return cursor.fetchall()

@db_common.connection_handler
def get_answers(cursor, question_id):
    query = f"SELECT *  \
            FROM answer\
            WHERE question_id = '{question_id}'"
    cursor.execute(query)
    return cursor.fetchall()

@db_common.connection_handler
def post_question(cursor, question_detail):
    cursor.execute("""INSERT INTO question
        (submission_time, view_number, vote_number, title, message, image)
        VALUES (%(s_t)s, %(v_w)s, %(v_e)s, %(t_e)s, %(m_e)s, %(i_e)s)""",
        {'s_t': question_detail['submission_time'],
         'v_w': question_detail['view_number'],
         'v_e': question_detail['vote_number'],
         't_e': question_detail['title'],
         'm_e': question_detail['message'],
         'i_e': question_detail['image']
         })

