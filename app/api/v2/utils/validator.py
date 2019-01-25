"""
    Validation Module
    Author: Kelyn Paul Njeri
"""
from flask_restplus import Namespace, fields
import re

class Validator:
    @staticmethod
    def check_input_for_null_entry(data):
        for value in data.values():
            return_value = True
            if value is "" or value is " ":
                return_value = False
                break
            else:
                return_value = True
        return return_value
        
    def check_valid_email_address(self, email):
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_pattern.match(email):
            return True
        else:
            return False

    def check_passwords_match(self, password1, password2):
        if password1 == password2:
            return True
        else:
            return False
    @staticmethod
    def check_for_space(data):
        error = None
        for key, value in data.items():
            if " " in value:
                error = "{} cannot contain spaces.".format(key)
        return True
    @staticmethod
    def check_password(password):
        if (len(password) < 6) or (len(password) > 12):
            return "Invalid Password"
        elif not re.search("[A-Z]", password):
            return "Invalid Password"
        elif not re.search("[a-z]", password):
            return "Invalid Password"
        elif not re.search("[0-9]", password):
            return "Invalid Password"
        elif not re.search(r"[^\w\*]", password):
            return "Invalid Password"
        elif not re.search(r"[^\s]", password):
            return "Invalid Password"
        else:
            return "Valid Password"
        