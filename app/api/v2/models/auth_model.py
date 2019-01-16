from ....database import initialize_db

db = initialize_db(config_name="development")
cursor = db.cursor()
class AuthModel():
    """Auth Model."""
    def register_user(self, data):
        query = """
        INSERT INTO users (firstname, lastname, othername, email, phone_number, username, registered, is_admin) VALUES (%(firstname)s, %(lastname)s, %(othername)s, %(email)s, %(phone_number)s, %(username)s, %(registered)s,%(is_admin)s);"""
        cursor.execute(query, data)
        db.commit()
        return data
    
    def find_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = {};".format(email)
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return "User already exists."
        return "User does not exist."

    def find_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = {};".format(username)
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return "User already exists."
        return "User does not exist."


