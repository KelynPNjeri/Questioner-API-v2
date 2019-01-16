"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response
from flask_restplus import reqparse, Resource


# Local Imports
from ..models.rsvp_model import RsvpModel
from ..utils.serializer import RsvpDataTransferObject

rsvp_api = RsvpDataTransferObject.rsvp_namespace

parser = reqparse.RequestParser()
# Meetup Arguments
parser.add_argument("meetup", type=int ,required=True, help="Please enter meetup location.")
parser.add_argument("user", type=int ,required=True, help="Please enter meetup image.")
parser.add_argument("response", type=str, help="Please enter meetup image.")

rsvp_request_model = RsvpDataTransferObject.rsvp_request_model

@rsvp_api.route('')
class Rsvp(Resource):
    @rsvp_api.expect(rsvp_request_model, validate=True)
    def post(self, meetup_id):
        """Creating an RSVP to an event."""
        request_data = parser.parse_args()
        user_id = request_data["user"]
        meetup_id = request_data["meetup"]
        response = request_data["response"]
            
        created_rsvp = RsvpModel(user_id, meetup_id, response)
        rsvp = created_rsvp.create_rsvp_record()
        response_payload = {
            "status": 201,
            "data": rsvp
        }
        response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
        return response

        


