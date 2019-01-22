from psycopg2.extras import RealDictCursor
from ..utils.helper import find_question_by_id
from ....database import initialize_db

db = initialize_db()
cursor = db.cursor(cursor_factory=RealDictCursor)

class RsvpModel():
    """Deals with Questions Operations."""
    def create_rsvp(self, data=None):
        query = """
        INSERT INTO rsvps (meetup_id, user_id, response) VALUES (%(meetup_id)s, %(user_id)s, %(response)s);"""
        cursor.execute(query, data)
        db.commit()
        return data
