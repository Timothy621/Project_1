class reimbursement:

    def __init__(self, event_type, modifier):
        self.modifier = modifier
        self.event_type = event_type

    def __repr__(self):
        str({
            'event_type': self.event_type,
            'modifier': self.modifier
            })

    def json(self):
        return{'eventType': self.event_type,
               'modifier': self.modifier
               }

