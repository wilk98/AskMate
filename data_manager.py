<<<<<<< HEAD
import db_common

QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


=======
from typing import List, Dict
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import db_common
>>>>>>> Maciek

@db_common.connection_handler
def read_questions(cursor):
    query = """
        SELECT *
        FROM question
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()
<<<<<<< HEAD
=======

@db_common.connection_handler
def get_question(cursor)
    query
>>>>>>> Maciek
