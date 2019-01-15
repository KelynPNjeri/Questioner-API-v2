"""
    Meetup Models
    Author: Kelyn Paul Njeri.
"""
from datetime import datetime
import json

from .base_model import BaseModel


class Meetup(BaseModel):
    """Models for meetup views."""

    def find_meetup_by_title(self, db, title):
        data_store = BaseModel.check_db(db)
        existing_meetup = [
            meetup for meetup in data_store if meetup["topic"] == title]
        if existing_meetup:
            return "Meetup already exists"

    def fetch_all_meetups(self):
        """Fetching all Meetup Records."""
        return BaseModel.retrieve_data(self, db="meetups")

    @staticmethod
    def create_an_rsvp(user_id, meetup_id, response):
        rsvps = []
        new_rsvp = dict(
            id=len(rsvps) + 1,
            user=user_id,
            meetup=meetup_id,
            status=response
        )
        rsvps.append(new_rsvp)
        return new_rsvp
