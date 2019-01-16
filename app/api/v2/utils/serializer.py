"""
    Serializer Module
    Author: Kelyn Paul Njeri
"""
from flask_restplus import Namespace, fields


class MeetupDataTransferObject():
    """Meetup Validators."""
    meetup_namespace = Namespace(
        "Meetup Endpoint",
        description="Responsible for creating, fetching, editing and deleting meetups."
    )

    meetup_request_model = meetup_namespace.model("Meetup Request Model", {
        "location": fields.String(description="The meetup location."),
        "images": fields.String(description="The URLs to the images of the meetup."),
        "topic": fields.String(description="The name of the meetup."),
        "happeningOn": fields.DateTime(dt_format='rfc822', description="Date when the event will be happening."),
        "Tags": fields.String(description="The meetup category.")

    })
class RsvpDataTransferObject():
    """Meetup Validators."""
    rsvp_namespace = Namespace(
        "RSVP Endpoint",
        description="Responsible for creating, fetching, editing and deleting RSVPs."
    )

    rsvp_request_model = rsvp_namespace.model("RSVP Request Model", {
        "meetup": fields.Integer(description="Id of specific meetup."),
        "user": fields.Integer(description="Id of specific user."),
        "response": fields.String(description="User's response to the RSVP.")
    })

class QuestionDataTransferObject():
    """Question Validators."""
    question_namespace = Namespace(
        "Question Endpoint",
        description="Responsible for creating, fetching, editing and deleting questions."
    )
    question_request_model = question_namespace.model("Question Request Model", {
        "user": fields.Integer(description="The user's id."),
        "meetup": fields.Integer(description="The meetup's ID."),
        "title": fields.String(description="The question's title."),
        "body": fields.String(description="The question's description.")

    })

class UserDataTransferObject():
    user_ns = Namespace("Authentication Endpoint", description="Responsible for registering and logging in users.")
    register_request_model = user_ns.model('User Registration Model', {
        "firstname": fields.String(description="User's first Name."),
        "lastname": fields.String(description="User's last Name."),
        "othername": fields.String(description="User's middle Name."),
        "email": fields.String(description="User's email."),
        "phoneNumber": fields.String(description="User's phone number."),
        "username": fields.String(description="User's username."),
        "password1": fields.String(description="User's password."),
        "password2": fields.String(description="User's confirmatory password.")

    })
    login_request_model = user_ns.model('User Login Model', {
        "username": fields.String(description="User's username."),
        "password": fields.String(description="User's password.")
    })
