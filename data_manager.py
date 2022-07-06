
import db_common



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
def search_question(cursor, ):
    query = """
        SELECT *
        FROM question
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()





