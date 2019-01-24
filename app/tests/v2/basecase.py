"""Base Case for all tests."""
import unittest
import json

# Local Import
from ... import create_app
from ...database import initialize_db, create_tables, drop_tables


class TestBaseCase(unittest.TestCase):
    """Base Testing Class."""
    def setUp(self):
        self.client = create_app(config_name="testing").test_client()
        # Initialize DB Connections.
        initialize_db()
        create_tables()
        self.content_type = "application/json"
        self.meetup_payload = {
            "location": "Nakuru",
            "image1": "www.google.com",
            "image2": "www.facebook.com",
            "image3": "www.pinterest.com",
            "topic": "Growing in tech",
            "happening_on": "2019-01-21",
            "description": "This is my event description.",
            "tag1": "Tech",
            "tag2": "Growth",
            "tag3": "Self-improvement"
        }
        self.meetup_payload_2 = {
            "location": "Nakuru",
            "image1": "www.google.com",
            "image2": "www.facebook.com",
            "image3": "www.pinterest.com",
            "topic": "Growth",
            "happening_on": "2019-01-21",
            "description": "This is my event description.",
            "tag1": "Tech",
            "tag2": "Growth",
            "tag3": "Self-improvement"
        }
        self.meetup_payload_3 = {
            "location": "Nakuru",
            "image1": "www.google.com",
            "image2": "www.facebook.com",
            "image3": "www.pinterest.com",
            "topic": "Technical Growth",
            "happening_on": "2019-01-29",
            "description": "This is my event description.",
            "tag1": "Tech",
            "tag2": "Growth",
            "tag3": "Self-improvement"
        }
        self.question_payload = {
            "user":  1,
            "meetup": 1,
            "title":  "Growing in tech?",
            "body":  "What is the main agenda of this meetup. Please clarify."
        }
        self.comment_payload = {
            "question_id":  1,
            "title":  "Growing in tech?",
            "body":  "What is the main agenda of this meetup. Please clarify."
        }
        self.rsvp_payload = {
            "user": 1,
            "meetup": 1,
            "response": "yes"
        }
        self.registration_payload = {
            "firstname": "Kelyn",
            "lastname": "Njeri",
            "othername": "Paul",
            "email": "example@gmail.com",
            "phoneNumber": "0722997807",
            "username": "testuser",
            "password1": "Test@12345",
            "password2": "Test@12345",
            "is_admin": "False"
        }
        self.login_payload = {
            "username": "testuser",
            "password": "Test@12345"
        }
        self.bad_login_payload = {
            "username": "testuser32",
            "password": "Test@19873"
        }
    def user_registration(self):
        return self.client.post('/api/v2/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
    def create_meetup(self):
        return self.client.post('/api/v2/meetups', data=json.dumps(self.meetup_payload), content_type=self.content_type)
    
    

        
    def tearDown(self):
        self.client = None
        self.content_type = None
        self.meetup_payload = None
        drop_tables()