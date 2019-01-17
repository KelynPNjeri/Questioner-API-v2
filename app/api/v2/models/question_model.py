from ....database import initialize_db

db = initialize_db(config_name="development")
cursor = db.cursor()

class QuestionModel():
    """Deals with Questions Operations."""
    def create_question(self, data=None):
        query = """
        INSERT INTO questions (created_by, meetup_id, title, body) VALUES (%(created_by)s, %(meetup_id)s, %(title)s, %(body)s);"""
        cursor.execute(query, data)
        db.commit()
        return data