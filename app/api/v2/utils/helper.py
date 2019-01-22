from psycopg2.extras import RealDictCursor

import json 

from ....database import initialize_db

db = initialize_db()
cursor = db.cursor(cursor_factory=RealDictCursor)
def find_user_by_email(email=None):
    query = "SELECT * FROM users WHERE email = '{}';".format(email)
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return "User already exists."
    return "User does not exist."

def find_user_by_username(username=None):
    query = "SELECT * FROM users WHERE username = '{}';".format(username)
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False

def find_meetup_by_id(meetup_id=None):
    query = "SELECT * FROM meetups WHERE id = '{}';".format(meetup_id)
    cursor.execute(query)
    meetups = cursor.fetchone()
    if meetups:
        meetups["created_on"] = str(meetups["created_on"])
        meetups["happening_on"] = str(meetups["happening_on"])
        return meetups
    return "Meetup doesn't exist."

def find_question_by_id(question_id=None):
    query = "SELECT * FROM questions WHERE id = '{}'".format(question_id)
    cursor.execute(query)
    question = cursor.fetchone()
    if question:
        return question
    return "Record doesn't exist."