import json

from .basecase import TestBaseCase as base
class TestAuthentication(base):
    """Testing Authentication endpoint"""
    def setUp(self):
        base.setUp(self)

    def test_user_registration(self):
        """Testing User Registration."""
        response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"], "User registered successfully. Please Log in.")
    
    def test_user_login(self):
        """Testing Logging In."""
        post_response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_data["message"], "User registered successfully. Please Log in.")
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.login_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data[0]["message"], "User login successful.")      

    def test_logging_in_non_existent_user(self):
        """Testing Logging in a non-existent user."""
        post_response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_data["message"], "User registered successfully. Please Log in.")
        response = self.client.post('/api/v1/auth/login', data=json.dumps(self.bad_login_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["error"], "User does not exist.")

    def testing_register_existing_user(self):
        response = self.client.post('/api/v1/auth/register', data=json.dumps(self.registration_payload), content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response_data["message"], "User already exists.")


        