"""
    Validation Module
    Author: Kelyn Paul Njeri
"""
import re 

class Validator:
    @staticmethod
    def check_input_for_null_entry(data):
        for key, value in data.items():
            if len(value) == 0:
                return "Field cannot be blank."
            elif value == " ":
                return "Field cannot be a space."
            else:
                return True

    def check_valid_email_address(self, email):
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if email_pattern.match(email):
            return True
        else:
            return "{} not an email.".format(email)

    def check_passwords_match(self, password1, password2):
        if password1 == password2:
            return True
        else:
            return "Passwords do not match."