"""Meetup Views Module"""
# Third Party Imports.
import json
from datetime import datetime
from flask import Response
from flask_restplus import reqparse, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local Imports
from ..models.meetup_model import MeetupModel
from ..utils.serializer import MeetupDataTransferObject
from ..utils.validator import Validator
from ..utils.helper import find_meetup_by_id, check_if_admin

meetup_api = MeetupDataTransferObject.meetup_namespace

parser = reqparse.RequestParser()
# Meetup Arguments
parser.add_argument("location", type=str, required=True,
                    help="Please enter meetup location.")
parser.add_argument("images", required=True, help="Please enter meetup image.", action="append")
parser.add_argument("topic", type=str, required=True,
                    help="Please enter meetup topic.")
parser.add_argument("happening_on", type=str, required=True,
                    help="Please enter meetup date.")
parser.add_argument("description", type=str, required=True,
                    help="Please add a meetup description.")
parser.add_argument("tags", required=True, help="Please enter meetup tag.", action="append")

meetup_request_model = MeetupDataTransferObject.meetup_request_model


@meetup_api.route('')
class MeetupList(Resource):
    """Meetup endpoint."""
    @meetup_api.expect(meetup_request_model)
    @jwt_required
    def post(self):
        """Performing a POST request."""
        current_user = get_jwt_identity()

        request_data = parser.parse_args()
        location = request_data["location"]
        images = request_data["images"]
        topic = request_data["topic"]
        happening_on = request_data["happening_on"]
        description = request_data["description"]
        tags = request_data["tags"]
        meetup_payload = dict(
            created_on=str(datetime.now()),
            location=location,
            images=images,
            topic=topic,
            happening_on=happening_on,
            description=description,
            tags=tags
        )
        is_admin = check_if_admin(username=current_user)
        check_payload = Validator.check_input_for_null_entry(data=meetup_payload)
       
        if check_payload:
            save_meetup = MeetupModel.create_meetup(self, data=meetup_payload)
            response_payload = dict(
                status=201,
                message="Meetup was created successfully.",
                data=save_meetup
            )
            response = Response(json.dumps(response_payload),
                                status=201, mimetype="application/json")
            return response
        error_payload = dict(
                status=400,
                error="Null fields.",
                message="Fields cannot be empty or spaces."
            )
        error_resp = Response(json.dumps(error_payload), status=400, mimetype="application/json")
        return error_resp
      
@meetup_api.route('/upcoming')
class GetMeetups(Resource):
    @jwt_required
    def get(self):
        """Fetching All Meetups"""
        meetups = MeetupModel.get_upcoming_meetups(self)
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
    @jwt_required
    def get(self, meetup_id):
        """Getting a specific meetup"""
        meetup = find_meetup_by_id(meetup_id=meetup_id)
        if meetup == "Meetup doesn't exist.":
            error_payload = dict(
                status=404,
                error=meetup,
                message="Please enter a valid meetup id."
            )
            response = Response(json.dumps(error_payload), status=404, mimetype="application/json")
            return response
        response_payload = {
            "status": 200,
            "data": meetup
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
    @jwt_required
    def delete(self, meetup_id):
        meetup = find_meetup_by_id(meetup_id=meetup_id)
        if meetup == "Meetup doesn't exist.":
            error_payload = dict(
                status=404,
                error=meetup,
                message="Please enter a valid meetup id."
            )
            response = Response(json.dumps(error_payload), status=404, mimetype="application/json")
            return response
        delete_meetup = MeetupModel().delete_meetup(meetup_id)
        response_payload = {
            "status": 200,
            "message": delete_meetup
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
        

