from psycopg2.extras import RealDictCursor
from ..utils.helper import find_question_by_id
from ....database import initialize_db

db = initialize_db()
cursor = db.cursor(cursor_factory=RealDictCursor)

class CommentModel():
    """Deals with Questions Operations."""
    def create_comment(self, data=None):
        query = """
        INSERT INTO comments (question_id, title, body, commented_on) VALUES (%(question_id)s, %(title)s, %(body)s, %(commented_on)s);"""
        cursor.execute(query, data)
        db.commit()
        return data
    
    def fetch_all_comments(self):
        query = "SELECT * FROM comments;"
        cursor.execute(query)
        comments = cursor.fetchall()
        return comments