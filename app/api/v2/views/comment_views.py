# Third Party Imports.
import json
from datetime import datetime
from flask_restplus import reqparse, Resource
from flask import Response

# Local Imports.
from ..models.comment_model import CommentModel
from ..utils.serializer import CommentDataTransferObject
from ..utils.validator import Validator

comment_api = CommentDataTransferObject.comment_namespace
parser = reqparse.RequestParser()
parser.add_argument("question_id", required=True, help="Enter the id to question being commented on.")
parser.add_argument("title", required=True, help="Add Comment Title.")
parser.add_argument("body", required=True, help="Add Comment Body.")

comment_request_model = CommentDataTransferObject.comment_request_model

@comment_api.route('')
class CommentList(Resource):
    def post(self):
        request_data = parser.parse_args()
        question_id = request_data["question_id"]
        title = request_data["title"]
        body = request_data["body"]

        comment_payload = dict(
            question_id=question_id,
            title=title,
            body=body,
            commented_on=str(datetime.now())
        )
        check_payload = Validator.check_input_for_null_entry(data=comment_payload)
        if check_payload:
            save_comment = CommentModel().create_comment(data=comment_payload)
            response_payload = dict(
            status=201,
            message="Comment was created successfully.",
            data=save_comment
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
        comments = CommentModel().fetch_all_comments()
        response_payload = {
            "status": 200,
            "data": comments
        }
        response = Response(json.dumps(response_payload),
                            status=200, mimetype="application/json")
        return response
