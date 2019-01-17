from ....database import initialize_db

db = initialize_db(config_name="development")
cursor = db.cursor()
class MeetupModel():
    """Deals with Meetup Operations."""
    def create_meetup(self, data=None):
        query = """
        INSERT INTO meetups (location, images, topic, happening_on, description, tags) VALUES (%(location)s, %(images)s, %(topic)s, %(happening_on)s, %(description)s, %(tags)s);"""
        cursor.execute(query, data)
        db.commit()
        return data