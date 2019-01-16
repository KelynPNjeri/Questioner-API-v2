class RsvpModel():
    rsvps = []
    def __init__(self, user_id, meetup_id, response):
        self.id = len(self.rsvps) + 1
        self.user = user_id
        self.meetup = meetup_id
        self.status = response

    def create_rsvp_record(self):
        rsvp_payload = dict(
            id=self.id,
            user=self.user,
            meetup=self.meetup,
            status=self.status
        )
        self.rsvps.append(rsvp_payload)
        return rsvp_payload
        
        