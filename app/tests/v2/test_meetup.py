"""Module for Testing the Meetup Endpoint."""
import json
from ddt import ddt, data

# Local Import
from .basecase import TestBaseCase as base

@ddt
class TestMeetup(base):
    """Testing the Meetup Endpoints with valid input."""

    def setUp(self):
        base.setUp(self)

    def test_create_meetup(self):
        """Testing Creation of a Meetup."""

        response = self.client.post(
            "/api/v1/meetups",
            data=json.dumps(self.meetup_payload),
            content_type=self.content_type,
        )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data["message"],
                         "Meetup was created successfully.")

    def test_fetching_all_meetups(self):
        """Testing Fetching of all meetups."""
        post_response = self.client.post(
            "/api/v1/meetups",
            data=json.dumps(self.meetup_payload),
            content_type=self.content_type
        )
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Meetup was created successfully."
        )
        response = self.client.get(
            "/api/v1/meetups/upcoming", content_type=self.content_type)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data["status"], 200)

    def test_fetch_single_meetup(self):
        """Test fetching a single meetup."""
        post_response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_payload_2), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Meetup was created successfully.")
        # Fetching Single Question.
        response = self.client.get(
            'api/v1/meetups/{}'.format(post_response_data["data"][0]["id"]), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    @data( 10, 20, 30)
    def test_fetch_non_existent_meetup(self, value):
        """Test fetching a single non-existent meetup."""
        post_response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_payload_2), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Meetup was created successfully.")
        # Fetching Single Question.
        response = self.client.get(
            'api/v1/meetups/{}'.format(value), content_type=self.content_type)
        self.assertEqual(response.status_code, 404)
        


    def test_rsvp_to_meetup(self):
        """Test RSVPing to a meetup."""
        """Test fetching a single meetup."""
        post_response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_payload), content_type=self.content_type)
        post_response_data = json.loads(post_response.data.decode())
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(
            post_response_data["message"], "Meetup was created successfully.")
        # Posting RSVP.
        response = self.client.post('/api/v1/meetups/{}/rsvps'.format(
            post_response_data["data"][0]["id"]), data=json.dumps(self.rsvp_payload), content_type=self.content_type)
        self.assertEqual(response.status_code, 201)

    # @data(20, 40, 50, 60)
    # def test_rsvp_to_non_existent_meetup(self, value):
    #     """Test RSVPing to a non-existent meetup."""
    #     post_response = self.client.post(
    #         '/api/v1/meetups', data=json.dumps(self.meetup_payload), content_type=self.content_type)
    #     post_response_data = json.loads(post_response.data.decode())
    #     self.assertEqual(post_response.status_code, 201)
    #     self.assertEqual(
    #         post_response_data["message"], "Meetup was created successfully.")
    #     # Posting RSVP.
    #     response = self.client.post('/api/v1/meetups/{}/rsvps'.format(
    #         value), data=json.dumps(self.rsvp_payload), content_type=self.content_type)
    #     self.assertEqual(response.status_code, 404)
