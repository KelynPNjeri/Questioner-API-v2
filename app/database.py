import psycopg2
import os


def initialize_db():
    """Creates Database Connection"""
    config = os.getenv("APP_SETTINGS")
    try:
        if config == "development":
            db_url = os.getenv("DB_DEVELOPMENT_URL")
            connection = psycopg2.connect(db_url)
            connection.autocommit = True
        elif config == "testing":
            db_url = os.getenv("DB_TESTING_URL")
            connection = psycopg2.connect(db_url)
            connection.autocommit = True
        return connection
    except Exception as e:
        return "{}, couldn't connect to database.".format(e)

    
    
def create_tables():
    """Creates tables"""
    user_table = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            othername VARCHAR(20) NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            phone_number VARCHAR(10) NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            password1 VARCHAR(20) NOT NULL,
            password2 VARCHAR(20) NOT NULL,
            registered VARCHAR NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE
        );
    """
    meetup_table = """
        CREATE TABLE IF NOT EXISTS meetups(
            id SERIAL PRIMARY KEY,
            created_on VARCHAR,
            location VARCHAR NOT NULL,
            images VARCHAR ARRAY NOT NULL,
            topic VARCHAR NOT NULL,
            happening_on VARCHAR NOT NULL,
            description VARCHAR(200) NOT NULL,
            tags VARCHAR ARRAY NOT NULL
        );
    """
    question_table = """
        CREATE TABLE IF NOT EXISTS questions(
            id SERIAL PRIMARY KEY,
            created_on VARCHAR,
            created_by INT NOT NULL,
            meetup_id INT NOT NULL,
            title VARCHAR NOT NULL,
            body VARCHAR NOT NULL,
            votes INT DEFAULT 0,
            FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (meetup_id) REFERENCES meetups(id) ON DELETE CASCADE
        );
    """
    votes_table = """
        CREATE TABLE IF NOT EXISTS votes(
            question_id INT,
            username VARCHAR,
            action VARCHAR,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
        );
    """
    comment_table = """
        CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            question_id INT NOT NULL,
            title VARCHAR NOT NULL,
            body VARCHAR NOT NULL,
            commented_on VARCHAR,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
        );
    """
    rsvp_table = """
        CREATE TABLE IF NOT EXISTS rsvps(
            id SERIAL PRIMARY KEY,
            meetup_id INT NOT NULL,
            user_id INT NOT NULL,
            response VARCHAR NOT NULL,
            FOREIGN KEY (meetup_id) REFERENCES meetups(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """
    add_citext = """CREATE EXTENSION IF NOT EXISTS citext;"""
    apply_citext = """ALTER TABLE users ALTER COLUMN username TYPE citext, ALTER COLUMN email TYPE citext;"""

    # super_admin = """
    #     INSERT INTO users (firstname, lastname, othername, email, phone_number, username, password1, password2, registered, is_admin) VALUES ('Draco', 'Trevor', 'David', 'adminemail@gmail.com', '0799688444', 'superadmin', 'pass1', 'pass2',25-01-2019, 'True');"""
    table_queries = [user_table, meetup_table, question_table, votes_table, comment_table, rsvp_table, add_citext, apply_citext]
    connection = initialize_db()
    for query in table_queries:
        cur = connection.cursor()
        cur.execute(query)
    connection.commit()
    connection.close()

def drop_tables():
    db = initialize_db()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS users CASCADE")
    cursor.execute("DROP TABLE IF EXISTS meetups CASCADE")
    cursor.execute("DROP TABLE IF EXISTS questions CASCADE")
    cursor.execute("DROP TABLE IF EXISTS votes CASCADE")
    cursor.execute("DROP TABLE IF EXISTS comments CASCADE")
    cursor.execute("DROP TABLE IF EXISTS rsvps CASCADE")