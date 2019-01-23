"""Module for Testing the Question Endpoints."""
import json
from ddt import ddt, data

# Local Import
from .basecase import TestBaseCase as base

@ddt
class TestComment(base):
    """Testing the Question Endpoints with valid input."""

    def setUp(self):
        base.setUp(self)

    def test_create_comment(self):
        """Testing Creation of a Comment."""
        self.user_registration()
        response = self.client.post(
            '/api/v2/comments', data=json.dumps(self.comment_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Comment was created successfully.")

    def test_fetch_all_questions(self):
        """Testing Creation of a Comment."""
        self.user_registration()
        response = self.client.post(
            '/api/v2/comments', data=json.dumps(self.comment_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Comment was created successfully.")
        # Fetching all questions.
        response = self.client.get(
            '/api/v2/comments', content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
