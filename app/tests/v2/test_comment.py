"""Module for Testing the Question Endpoints."""
import json

# Local Import
from .basecase import TestBaseCase as base

class TestComment(base):
    """Testing the Question Endpoints with valid input."""

    def setUp(self):
        base.setUp(self)

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
