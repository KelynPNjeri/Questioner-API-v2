"""Module for Testing the Question Endpoints."""
import json

# Local Import
from .basecase import TestBaseCase as base

class TestComment(base):
    """Testing the Question Endpoints with valid input."""

    def setUp(self):
        super().setUp()
        

    def login_user(self):
        register = self.client.post('/api/v2/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        user_login = self.client.post('/api/v2/auth/login', data=json.dumps(self.login_payload), content_type=self.content_type)
        login_data = json.loads(user_login.data.decode('utf-8'))
        token = login_data['auth_token']
        return token
      

    def test_create_comment(self):
        """Testing Creation of a Comment."""
        create_meetup = self.client.post(
            '/api/v2/meetups', data=json.dumps(self.meetup_payload), headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)
        create_question = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)     
        response = self.client.post('/api/v2/comments', data=json.dumps(self.comment_payload), headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Comment was created successfully.")

    def test_fetch_all_comments(self):
        """Testing Creation of a Comment."""
        # Create a question.
        create_question = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)
        response = self.client.post(
            '/api/v2/comments', data=json.dumps(self.comment_payload), headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Comment was created successfully.")
        # Fetching all questions.
        response = self.client.get(
            '/api/v2/comments', headers=dict(Authorization="Bearer "+ self.login_user()), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
