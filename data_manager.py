import sqlite3
import db_common


@db_common.connection_handler
def read_questions(cursor):
    query = """
        SELECT id, submission_time, view_number, vote_number,
                title, message, image
        FROM question
        ORDER BY vote_number DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@db_common.connection_handler
def get_question(cursor, question_id):
    query = """SELECT *
            FROM question
            WHERE id = %s"""
    cursor.execute(query, (question_id,))
    return cursor.fetchone()


@db_common.connection_handler
def get_answers(cursor, question_id):
    query = """SELECT *
            FROM answer
            WHERE question_id = %s"""
    cursor.execute(query, (question_id,))
    return cursor.fetchall()


@db_common.connection_handler
def get_answer(cursor, answer_id):
    query = """SELECT *
        FROM answer
        WHERE id = %s"""
    cursor.execute(query, (answer_id,))
    return cursor.fetchone()


@db_common.connection_handler
def get_comment_answer(cursor, answer_id):
    query = """SELECT *
        FROM comment
        WHERE answer_id = %s"""
    cursor.execute(query, (answer_id,))
    return cursor.fetchall()


@db_common.connection_handler
def get_comment_question(cursor, question_id):
    query = """SELECT *
        FROM comment
        WHERE question_id = %s"""
    cursor.execute(query, (question_id,))
    return cursor.fetchall()


@db_common.connection_handler
def get_comment(cursor, comment_id):
    query = """SELECT *
        FROM comment
        WHERE id = %s"""
    cursor.execute(query, (comment_id,))
    return cursor.fetchone()


@db_common.connection_handler
def get_tag_id(cursor, question_id):
    query = """SELECT tag_id
        FROM question_tag
        WHERE question_id = %s"""
    cursor.execute(query, (question_id,))
    return cursor.fetchall()


@db_common.connection_handler
def get_tag(cursor, tag_id):
    query = """SELECT name
        FROM tag
        WHERE id = %s"""
    cursor.execute(query, (tag_id,))
    return cursor.fetchall()


@db_common.connection_handler
def post_question(cursor, question_detail):
    cursor.execute("""INSERT INTO question
        (submission_time, view_number, vote_number, title, message, image, member_id)
        VALUES (%(s_t)s, %(v_w)s, %(v_e)s, %(t_e)s, %(m_e)s, %(i_e)s, %(m_i)s)""",
                   {'s_t': question_detail['submission_time'],
                    'v_w': question_detail['view_number'],
                    'v_e': question_detail['vote_number'],
                    't_e': question_detail['title'],
                    'm_e': question_detail['message'],
                    'i_e': question_detail['image'],
                    'm_i': question_detail['member_id']
                    })


@db_common.connection_handler
def post_answer(cursor, answer):
    cursor.execute("""INSERT INTO answer\
    (submission_time, vote_number, question_id, message, image, member_id)
    VALUES (%(s_t)s, %(v_n)s, %(q_i)s, %(m_e)s, %(i_e)s, %(m_i)s)""",
                   {
                       's_t': answer['submission_time'],
                       'v_n': answer['vote_number'],
                       'q_i': answer['question_id'],
                       'm_e': answer['message'],
                       'i_e': answer['image'],
                       'm_i': answer['member_id']
                   })


@db_common.connection_handler
def post_comment_answer(cursor, comment):
    cursor.execute("""INSERT INTO comment
        (answer_id, message, submission_time, edited_count, member_id)
        VALUES ( %(a_i)s, %(m_e)s, %(s_t)s, %(e_c)s, %(m_i)s)""",
                   {
                       'a_i': comment['answer_id'],
                       'm_e': comment['message'],
                       's_t': comment['submission_time'],
                       'e_c': comment['edited_count'],
                       'm_i': comment['member_id']
                   })


@db_common.connection_handler
def post_comment_question(cursor, comment):
    cursor.execute("""INSERT INTO comment
        (question_id, message, submission_time, edited_count, member_id)
        VALUES ( %(q_i)s, %(m_e)s, %(s_t)s, %(e_c)s, %(m_i)s)""",
                   {
                       'q_i': comment['question_id'],
                       'm_e': comment['message'],
                       's_t': comment['submission_time'],
                       'e_c': comment['edited_count'],
                       'm_i': comment['member_id']
                   })


@db_common.connection_handler
def delete_question(cursor, question_id):
    query = """DELETE FROM question
        WHERE id = %s"""
    return cursor.execute(query, (question_id,))


@db_common.connection_handler
def delete_answers(cursor, question_id):
    query = """DELETE FROM answer
        WHERE question_id = %s"""
    return cursor.execute(query, (question_id,))


@db_common.connection_handler
def delete_answer(cursor, answer_id):
    query = """DELETE FROM answer
        WHERE id = %s"""
    return cursor.execute(query, (answer_id,))


@db_common.connection_handler
def delete_comment(cursor, comment_id):
    query = """DELETE FROM comment
        WHERE id = %s"""
    return cursor.execute(query, (comment_id,))


@db_common.connection_handler
def vote_question_up(cursor, question_id):
    query = """UPDATE question
        SET vote_number = vote_number + 1
        WHERE id = %s"""
    return cursor.execute(query, (question_id,))


@db_common.connection_handler
def vote_question_down(cursor, question_id):
    query = """UPDATE question
        SET vote_number = vote_number - 1
        WHERE id = %s"""
    return cursor.execute(query, (question_id,))


@db_common.connection_handler
def vote_answer_up(cursor, answer_id):
    query = """UPDATE answer
        SET vote_number = vote_number + 1
        WHERE id = %s"""
    return cursor.execute(query, (answer_id,))


@db_common.connection_handler
def vote_answer_down(cursor, answer_id):
    query = """UPDATE answer
        SET vote_number = vote_number - 1
        WHERE id = %s"""
    return cursor.execute(query, (answer_id,))


@db_common.connection_handler
def edit_question(cursor, question_to_edit):
    query = f"UPDATE question\
        SET title = '{question_to_edit['title']}', " \
            f"message = '{question_to_edit['message']}', image = '{question_to_edit['image']}'\
        WHERE id = '{question_to_edit['id']}';"
    return cursor.execute(query)


@db_common.connection_handler
def edit_answer(cursor, answer_to_edit):
    query = f"UPDATE answer\
        SET message = '{answer_to_edit['message']}', image = '{answer_to_edit['image']}'\
        WHERE id = '{answer_to_edit['id']}';"
    return cursor.execute(query)


@db_common.connection_handler
def edit_comment(cursor, comment_to_edit):
    query = f"UPDATE comment\
        SET message = '{comment_to_edit['message']}'\
        WHERE id = '{comment_to_edit['id']}';"
    return cursor.execute(query)


@db_common.connection_handler
def add_tag(cursor, new_tag, question_id):
    cursor.execute(f"""INSERT INTO tag
        (name)
        VALUES ('{new_tag}')""")
    cursor.execute(f"""INSERT INTO question_tag
            (question_id, tag_id)
            VALUES ('{question_id}', (SELECT id FROM tag WHERE name='{new_tag}'))""")


@db_common.connection_handler
def get_question_by_column(cursor, column_select, order):
    # TODO: check column_select value to avoid SQL Injection!
    allowed_columns = ['title', 'submission_time', 'view_number', 'vote_number', 'message']
    if column_select not in allowed_columns:
        column_select = 'title'
    query = """
            SELECT id, submission_time, view_number, vote_number,
                    title, message, image
            FROM question
            ORDER BY """
    query += column_select
    if order and order in ['asc', 'desc']:
        query += " " + order
    cursor.execute(query)
    return cursor.fetchall()


@db_common.connection_handler
def get_search(cursor, q):
    cursor.execute("""SELECT *
                      FROM
                      question
                      WHERE title ILIKE %(q1)s""", {'q1': f"%{q}%"})
    return cursor.fetchall()


@db_common.connection_handler
def addUser(cursor, new_user):
    print(new_user)
    cursor.execute("""INSERT INTO member(user_name, password, registration_date)
                   VALUES (%(e_m)s, %(p_s)s, %(t_m)s )""",
                   {
                       'e_m': new_user['user_name'],
                       'p_s': new_user['password'],
                       't_m': new_user['registration_date']
                   })


@db_common.connection_handler
def check_user(cursor, user_data):
    cursor.execute("""SELECT member_id FROM member
                        WHERE user_name = %(username)s AND password = %(psw)s""",
                        {
                            'username': user_data['user_name'],
                            'psw': user_data['password']
                        })
    return cursor.fetchone()