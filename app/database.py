import psycopg2
import os

from instance.config import APP_CONFIG



def initialize_db(config_name):
    url = APP_CONFIG[config_name].DATABASE_URL
    connection = psycopg2.connect(url)
    return connection
    
def create_tables():
    user_table = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            othername VARCHAR(20) NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            phone_number VARCHAR(10) UNIQUE NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            registered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            is_admin BOOLEAN NOT NULL DEFAULT FALSE
        );
    """
    meetup_table = """
        CREATE TABLE IF NOT EXISTS meetups(
            id SERIAL PRIMARY KEY,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            location VARCHAR NOT NULL,
            images VARCHAR ARRAY NOT NULL,
            topic VARCHAR NOT NULL,
            happening_on DATE NOT NULL,
            tags VARCHAR ARRAY NOT NULL
        );
    """
    question_table = """
        CREATE TABLE IF NOT EXISTS questions(
            id SERIAL PRIMARY KEY,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            created_by INT NOT NULL,
            meetup_id INT NOT NULL,
            title VARCHAR NOT NULL,
            body VARCHAR NOT NULL,
            votes INT,
            FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (meetup_id) REFERENCES meetups(id) ON DELETE CASCADE,
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
    table_queries = [user_table, meetup_table, question_table, rsvp_table]
    development_stage = os.getenv("APP_SETTINGS")
    conn = initialize_db(config_name=development_stage)
    for query in table_queries:
        cur = conn.cursor()
        cur.execute(query)
    conn.commit()
    conn.close()
