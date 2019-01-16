"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response
from flask_restplus import reqparse, Resource
from werkzeug.exceptions import NotFound

# Local Imports
from ..models.meetup_model import Meetup
from ..utils.serializer import MeetupDataTransferObject

meetup_api = MeetupDataTransferObject.meetup_namespace

parser = reqparse.RequestParser()
# Meetup Arguments
parser.add_argument("location", type=str, required=True,
                    help="Please enter meetup location.")
parser.add_argument("image1", required=True, help="Please enter meetup image.")
parser.add_argument("image2", help="Please enter meetup image.")
parser.add_argument("image3", help="Please enter meetup image.")
parser.add_argument("topic", type=str, required=True,
                    help="Please enter meetup topic.")
parser.add_argument("happening_on", type=str, required=True,
                    help="Please enter meetup date.")
parser.add_argument("description", type=str, required=True,
                    help="Please add a meetup description.")
parser.add_argument("tag1", required=True, help="Please enter meetup tag.")
parser.add_argument("tag2", required=True, help="Please enter meetup tag.")
parser.add_argument("tag3", required=True, help="Please enter meetup tag.")

meetup_request_model = MeetupDataTransferObject.meetup_request_model


@meetup_api.route('')
class MeetupList(Resource):
    """Meetup endpoint."""
    @meetup_api.expect(meetup_request_model, validate=True)
    def post(self):
        """Performing a POST request."""
        request_data = parser.parse_args()
        location = request_data["location"]
        image1 = request_data["image1"]
        image2 = request_data["image2"]
        image3 = request_data["image3"]
        topic = request_data["topic"]
        happening_on = request_data["happening_on"]
        description = request_data["description"]
        tag1 = request_data["tag1"]
        tag2 = request_data["tag2"]
        tag3 = request_data["tag3"]

        images = [image1, image2, image3]
        tags = [tag1, tag2, tag3]

        meetup_payload = dict(
            location=location,
            images=images,
            topic=topic,
            happening_on=happening_on,
            description=description,
            tags=tags
        )
        save_meetup = Meetup.save_data(self, db="meetups", data=meetup_payload)
        response_payload = dict(
            status=201,
            message="Meetup was created successfully.",
            data=save_meetup
        )
        response = Response(json.dumps(response_payload),
                            status=201, mimetype="application/json")
        return response


@meetup_api.route('/upcoming')
class GetMeetups(Resource):
    def get(self):
        """Fetching All Meetups"""
        meetups = Meetup.fetch_all_meetups(self)
        response_payload = {
            "status": 200,
            "data": meetups
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response


@meetup_api.route('/<int:meetup_id>')
class SingleMeetup(Resource):
    """Deals with operations on single meetup record."""

    def get(self, meetup_id):
        """Getting a specific meetup"""
        meetup = Meetup.find_by_id(self, db="meetups", id=meetup_id)
        if meetup == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error=meetup,
                message="Please enter a valid meetup id."
            )
            error = NotFound()
            error.data = error_payload
            raise error
        response_payload = {
            "status": 200,
            "data": meetup
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
