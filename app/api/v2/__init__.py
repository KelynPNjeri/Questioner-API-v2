"""Version 1 API module."""

# Third party imports
from flask_restplus import Api
from flask import Blueprint

# Local Imports
from .views.meetup_views import meetup_api
from .views.question_views import question_api
from .views.auth_views import auth_api
from .views.rsvp_views import rsvp_api
from .views.comment_views import comment_api

version2 = Blueprint('Questioner version 2', __name__, url_prefix="/api/v2")

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }}

api = Api(version2, version="2.0", title="Questioner REST API",
          description="This is backend of the Questioner Web app.", doc="/documentation", authorizations=authorizations)

api.add_namespace(meetup_api, path="/meetups")
api.add_namespace(question_api, path="/questions")
api.add_namespace(auth_api, path="/auth")
api.add_namespace(rsvp_api, path="/meetups/<int:meetup_id>/rsvps")
api.add_namespace(comment_api, path="/comments")
