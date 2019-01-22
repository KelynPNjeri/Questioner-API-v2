"""Question Views Module."""
# Third Party Imports.
import json
from datetime import datetime
from flask_restplus import reqparse, Resource
from flask import Response
from werkzeug.exceptions import NotFound

# Local Imports.
from ..models.question_model import QuestionModel
from ..utils.serializer import QuestionDataTransferObject
from ..utils.validator import Validator
from ..utils.helper import find_question_by_id

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

    def patch(self, question_id):
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

        upvote_question = QuestionModel().upvote_question(question_id)
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

    def patch(self, question_id):
        question = QuestionModel()
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Invalid question id",
                message="Please enter a valid question id"
            )
            error = NotFound()
            error.data = error_payload
            raise error

        downvote_question = QuestionModel()
        response_payload = {
            "status": 200,
            "data": downvote_question
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
