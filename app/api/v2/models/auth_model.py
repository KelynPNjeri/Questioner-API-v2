from ....database import initialize_db

db = initialize_db()
cursor = db.cursor()
class AuthModel():
    """Auth Model."""
    def register_user(self, data):
        query = """
        INSERT INTO users (firstname, lastname, othername, email, phone_number, username, password1, password2, registered) VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(email)s, %(phone_number)s, %(username)s, %(password1)s, %(password2)s,%(registered)s);"""
        cursor.execute(query, data)
        db.commit()
        query2 = "SELECT * FROM users "
        return data