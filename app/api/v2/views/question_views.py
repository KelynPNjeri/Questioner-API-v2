"""Question Views Module."""
# Third Party Imports.
import json
from datetime import datetime
from flask_restplus import reqparse, Resource
from flask import Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.exceptions import NotFound

# Local Imports.
from ..models.question_model import QuestionModel
from ..utils.serializer import QuestionDataTransferObject
from ..utils.validator import Validator
from ..utils.helper import find_question_by_id, check_for_votes, save_vote

question_api = QuestionDataTransferObject.question_namespace

parser = reqparse.RequestParser()
parser.add_argument("user", required=True, help="Enter the user id.")
parser.add_argument("meetup", required=True, help="Enter the meetup id.")
parser.add_argument("title", required=True, help="Add Question Title.")
parser.add_argument("body", required=True, help="Add Question Body.")

question_request_model = QuestionDataTransferObject.question_request_model


@question_api.route('')
class QuestionList(Resource):
    """Question Endpoint."""
    @question_api.expect(question_request_model, validate=True)
    @jwt_required
    def post(self):
        """POST request."""
        request_data = parser.parse_args()
        created_by = request_data["user"]
        meetup_id = request_data["meetup"]
        title = request_data["title"]
        body = request_data["body"]
        new_question = dict(
            created_on=str(datetime.now()),
            created_by=created_by,
            meetup_id=meetup_id,
            title=title,
            body=body
        )
        check_payload = Validator.check_input_for_null_entry(data=new_question)
        if check_payload:
            save_question = QuestionModel.create_question(self, data=new_question)
            response_payload = dict(
                status=201,
                message="Question was created successfully.",
                data=save_question
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
    @jwt_required
    def get(self):
        """Fetch All Questions."""
        questions = QuestionModel().retrieve_all_questions()
        response_payload = {
            "status": 200,
            "data": questions
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response


@question_api.route('/<int:question_id>')
class SingleQuestions(Resource):
    """Deals with all operations on specific questions."""
    @jwt_required
    def get(self, question_id):
        question = find_question_by_id(question_id=question_id)
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Invalid question id",
                message="Please enter a valid question id"
            )
            error = NotFound()
            error.data = error_payload
            raise error

        response_payload = {
            "status": 200,
            "data": question
        }
        # Response
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response


@question_api.route('/<int:question_id>/upvote')
class Upvote(Resource):
    """Deals with question upvote."""
    @jwt_required
    def patch(self, question_id):
        current_user = get_jwt_identity()
        check_if_voted = check_for_votes(question_id=question_id, username=current_user, action="upvote")
        if check_if_voted:
            error_payload = dict(
                status=403,
                error="Attempting to upvote twice.",
                message="User can only upvote once."
            )
            resp = Response(json.dumps(error_payload), status=403, mimetype="application/json")
            return resp
        question = find_question_by_id(question_id=question_id)
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Question does not exist.",
                message="Please enter a valid question id"
            )
            resp = Response(json.dumps(error_payload), status=404, mimetype="application/json")
            return resp
        upvote_question = QuestionModel().upvote_question(question_id)
        votes_payload = dict(
            question_id=question_id,
            username=current_user,
            action="upvote"
        )
        save_vote(data=votes_payload)
        response_payload = {
            "status": 200,
            "data": upvote_question
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response


@question_api.route('/<int:question_id>/downvote')
class Downvote(Resource):
    """Deals with question downvote."""
    @jwt_required
    def patch(self, question_id):
        current_user = get_jwt_identity()
        check_if_voted = check_for_votes(question_id=question_id, username=current_user, action="downvote")
        if check_if_voted:
            error_payload = dict(
                status=403,
                error="Attempting to downvote twice.",
                message="User can only downvote once."
            )
            resp = Response(json.dumps(error_payload), status=403, mimetype="application/json")
            return resp
        question = find_question_by_id(question_id=question_id)
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Invalid question id",
                message="Please enter a valid question id"
            )
            resp = Response(json.dumps(error_payload), status=404, mimetype="application/json")
            return resp
        downvote_question = QuestionModel().downvote_question(question_id)
        votes_payload = dict(
            question_id=question_id,
            username=current_user,
            action="downvote"
        )
        save_vote(data=votes_payload)
        response_payload = {
            "status": 200,
            "data": downvote_question
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
