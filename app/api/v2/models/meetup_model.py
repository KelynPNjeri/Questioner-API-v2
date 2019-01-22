from psycopg2.extras import RealDictCursor
from ....database import initialize_db

db = initialize_db()
cursor = db.cursor(cursor_factory=RealDictCursor)
class MeetupModel():
    """Deals with Meetup Operations."""
    def create_meetup(self, data=None):
        query = """
        INSERT INTO meetups (location, images, topic, happening_on, description, tags) VALUES (%(location)s, %(images)s, %(topic)s, %(happening_on)s, %(description)s, %(tags)s);"""
        cursor.execute(query, data)
        db.commit()
        return data
    def get_upcoming_meetups(self):
        query = "SELECT * FROM meetups;"
        cursor.execute(query)
        meetups = cursor.fetchall()
        return meetups

    def delete_meetup(self, meetup_id):
        query = "DELETE FROM meetups WHERE id = '{}';".format(meetup_id)
        cursor.execute(query)
        db.commit()
        return "Meetup deleted successfully."