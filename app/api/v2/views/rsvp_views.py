"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response
from flask_restplus import reqparse, Resource
from flask_jwt_extended import jwt_required


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
        acceptable_resp = ["yes", "no"]
        validate_resp = [resp for resp in acceptable_resp if resp == response]
        
        if validate_resp:    
            rsvp_payload = dict(
                meetup_id=meetup_id,
                user_id=user_id,
                response=response
            )
            rsvp = RsvpModel().create_rsvp(data=rsvp_payload)
            response_payload = {
                "status": 201,
                "data": rsvp
            }
            response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
            return response
        error_payload = dict(
            error="Invalid response input!",
            msg="Please enter 'yes' or 'no' as a response."
        )
        resp = Response(json.dumps(error_payload), status=400, mimetype="application/json")
        return resp
        


