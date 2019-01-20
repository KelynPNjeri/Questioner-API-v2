from ....database import initialize_db

db = initialize_db()
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

def find_meetup_by_id(meetup_id=None):
    query = "SELECT json_agg(row_to_json((SELECT ColumnName FROM (SELECT id, created_on, location, images, topic, happening_on, description, tags) AS ColumnName (id, created_on, location, images, topic, happening_on, description, tags)))) AS JsonData FROM meetups WHERE id = '{}';".format(meetup_id)
    cursor.execute(query)
    meetups = cursor.fetchone()
    if meetups:
        return meetups
    return "Meetup doesn't exist."