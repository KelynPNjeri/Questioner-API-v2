"""Auth Views."""
import json
from flask import Response
from flask_restplus import reqparse, Resource
from werkzeug.exceptions import BadRequest, NotFound

# Local Imports
from ..models.auth_model import AuthModel
from ..utils.serializer import UserDataTransferObject
from ..utils.validator import Validator

auth_api = UserDataTransferObject.user_ns

parser = reqparse.RequestParser()
parser.add_argument('firstname', type=str, help="Fill in first name.")
parser.add_argument('lastname', type=str, help="Fill in last name.")
parser.add_argument('othername', type=str, help="Fill in other name.")
parser.add_argument('email', type=str, help="Fill in email.")
parser.add_argument('phoneNumber', type=str, help="Fill in phone number.")
parser.add_argument('username', type=str, help="Fill in username.")
parser.add_argument('password1', type=str, help="Fill in password1.")
parser.add_argument('password2', type=str, help="Fill in password2.")

register_request_model = UserDataTransferObject.register_request_model

@auth_api.route("/register")
class RegisterUser(Resource):
    """User Registration"""
    @auth_api.expect(register_request_model, validate=True)
    def post(self):
        """Registering a User"""
        request_data = parser.parse_args()
        firstname = request_data["firstname"]
        lastname = request_data["lastname"]
        othername = request_data["othername"]
        email = request_data["email"]
        phone_number = request_data["phoneNumber"]
        username = request_data["username"]
        password1 = request_data["password1"]
        password2 = request_data["password2"]
        # Validations
        validate_email = Validator.check_valid_email_address(self, email)
        matching_passwords = Validator.check_passwords_match(self, password1, password2)
        if validate_email and matching_passwords:
            register_payload = dict(
                firstname=firstname,
                lastname=lastname,
                othername=othername,
                email=email,
                phoneNumber=phone_number,
                username=username,
                password1=password1,
                password2=password2
            )
            check_payload = Validator.check_input_for_null_entry(register_payload)
            if check_payload:
                register_user = AuthModel.save_data(self, db="users", data=register_payload)
                response = Response(json.dumps(register_user), status=201, mimetype="application/json")
                return response
            error_payload = dict(
                status=400,
                error=check_payload,
                message="Fields cannot be empty."
            )
            error_resp = Response(json.dumps(error_payload), status=400, mimetype="application/json")
            return error_resp
        error_payload = dict(
            status="400",
            error="Error with either your email or password",
            message="Check password and email."
        )
        error = BadRequest()
        error.data = error_payload
        raise error
@auth_api.route('/login')
class LoginUser(Resource):
    """User Login."""
    def post(self):
        """Log In."""
        request_data = parser.parse_args()
        username = request_data["username"]
        password = request_data["password1"]
        login_payload = dict(
            username=username,
            password=password
        )
        login = {
            "status": 200,
            "message": "User Logged in successfully" 
            
        }
        response = Response(json.dumps(login), status=200, mimetype="application/json")
        return response

    

