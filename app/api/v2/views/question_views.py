"""Question Views Module."""
# Third Party Imports.
import json
from flask_restplus import reqparse, Resource
from flask import Response
from werkzeug.exceptions import NotFound

# Local Imports.
from ..models.question_model import QuestionModel
from ..utils.serializer import QuestionDataTransferObject

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
        user = request_data["user"]
        meetup = request_data["meetup"]
        title = request_data["title"]
        body = request_data["body"]
        new_question = dict(
            user=user,
            meetup=meetup,
            title=title,
            body=body
        )
        save_question = QuestionModel.create_question_record(
            self, data=new_question)
        response_payload = dict(
            status=201,
            message="Question was created successfully.",
            data=save_question
        )
        response = Response(json.dumps(response_payload),
                            status=201, mimetype="application/json")
        return response

    def get(self):
        """Fetch All Questions."""
        questions = QuestionModel.fetch_all_questions(self)
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
        question = QuestionModel.fetch_specific_question(self, question_id)
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
        question = QuestionModel.fetch_specific_question(self, question_id)
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Invalid question id",
                message="Please enter a valid question id"
            )
            error = NotFound()
            error.data = error_payload
            raise error

        upvote_question = QuestionModel.upvote_question(
            self, question=question)
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
        question = QuestionModel.fetch_specific_question(self, question_id)
        if question == "Record doesn't exist.":
            error_payload = dict(
                status=404,
                error="Invalid question id",
                message="Please enter a valid question id"
            )
            error = NotFound()
            error.data = error_payload
            raise error

        downvote_question = QuestionModel.downvote_question(self, question)
        response_payload = {
            "status": 200,
            "data": downvote_question
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
