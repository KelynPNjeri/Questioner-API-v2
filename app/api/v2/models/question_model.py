"""
    Question Models
    Author: Kelyn Paul Njeri.
"""
import json
from datetime import datetime

from .base_model import BaseModel


class QuestionModel(BaseModel):
    """Question Model."""

    def create_question_record(self, data):
        """Creating Question Record."""
        return BaseModel.save_data(self, db="questions", data=data)

    def fetch_all_questions(self):
        """Fetching all questions."""
        return BaseModel.retrieve_data(self, db="questions")

    def fetch_specific_question(self, question_id):
        """Fetching Specific Questions"""
        return BaseModel.find_by_id(self, db="questions", id=question_id)

    def upvote_question(self, question):
        """Upvote question"""
        question[0]["votes"] = question[0]["votes"] + 1
        return question

    def downvote_question(self, question):
        """Downvote question"""
        question[0]["votes"] = question[0]["votes"] - 1
        return question
