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
    def get_upcoming_meetups(self):
        query = "SELECT json_agg(row_to_json((SELECT ColumnName FROM (SELECT id, created_on, location, images, topic, happening_on, description, tags) AS ColumnName (id, created_on, location, images, topic, happening_on, description, tags)))) AS JsonData FROM meetups;"
        cursor.execute(query)
        meetups = cursor.fetchall()
        return meetups