from ....database import initialize_db

db = initialize_db(config_name="development")
cursor = db.cursor()
def find_user_by_email(email=None):
    query = "SELECT firstname, lastname, othername, email, phone_number, username FROM users WHERE email = '{}';".format(email)
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return "User already exists."
    return "User does not exist."

def find_user_by_username(username=None):
    query = "SELECT firstname, lastname, othername, email, phone_number, username, password1 FROM users WHERE username = '{}';".format(username)
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return True
    return False


