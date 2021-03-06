from psycopg2.extras import RealDictCursor
from ..utils.helper import find_question_by_id
from ....database import initialize_db

db = initialize_db()
cursor = db.cursor(cursor_factory=RealDictCursor)

class QuestionModel():
    """Deals with Questions Operations."""
    def create_question(self, data=None):
        query = """
        INSERT INTO questions (created_on, created_by, meetup_id, title, body) VALUES (%(created_on)s, %(created_by)s, %(meetup_id)s, %(title)s, %(body)s);"""
        cursor.execute(query, data)
        db.commit()
        return data

    def retrieve_all_questions(self):
        query = "SELECT * FROM questions;"
        cursor.execute(query)
        questions = cursor.fetchall()
        return questions

    def upvote_question(self, question_id):
        query = "UPDATE questions SET votes = votes + 1 WHERE id = '{}';".format(question_id)
        cursor.execute(query)
        question = find_question_by_id(question_id=question_id)
        return question

    def downvote_question(self, question_id):
        query = "UPDATE questions SET votes = votes - 1 WHERE id = '{}';".format(question_id)
        cursor.execute(query)
        question = find_question_by_id(question_id=question_id)
        return question

