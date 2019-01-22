"""Module for Testing the Question Endpoints."""
import json
from ddt import ddt, data

# Local Import
from .basecase import TestBaseCase as base

@ddt
class TestQuestion(base):
    """Testing the Question Endpoints with valid input."""

    def setUp(self):
        base.setUp(self)

    def test_create_question(self):
        """Testing Creation of a Question."""
        self.user_registration()
        self.create_meetup()
        response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Question was created successfully.")

    def test_fetch_all_questions(self):
        """Test fetching all questions."""
        self.user_registration()
        self.create_meetup()
        post_response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Question was created successfully.")
        # Fetching all questions.
        response = self.client.get(
            '/api/v2/questions', content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_question(self):
        """Test fetching a single question."""
        self.user_registration()
        self.create_meetup()
        post_response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Question was created successfully.")
        # Fetching Single Question.
        response = self.client.get('api/v2/questions/1', content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    @data(20, 30, 40, 50)
    def test_fetch_non_existent_question(self, value):
        """Test fetching non existent data."""
        self.user_registration()
        self.create_meetup()
        post_response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Question was created successfully.")
        # Fetching Single Question.
        response = self.client.get('api/v2/questions/{}'.format(
            value), content_type=self.content_type)
        self.assertEqual(response.status_code, 404)


    def test_question_upvote(self):
        """Test upvoting a question."""
        self.user_registration()
        self.create_meetup()
        post_response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        print(post_response_data)
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Question was created successfully.")
        # Fetching Single Question.
        response = self.client.patch(
            'api/v2/questions/1/upvote', content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["data"][0]["votes"], 1)

    def test_downvote(self):
        """Testing downvoting a question."""
        self.user_registration()
        self.create_meetup()
        post_response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.question_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Question was created successfully.")
        # Fetching Single Question.
        response = self.client.patch('api/v2/questions/1/downvote', content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["data"][0]["votes"], -1)

