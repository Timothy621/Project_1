
class Request:
    def __init__(self, requestid, employee_id, event_type='', event_date=0, event_time=0, event_location='',
                 event_cost=0.00, event_reimbersment=0.00, evemt_grading_type='', employee_grade='',
                 request_status='pending supervisor', event_description=''):
        self.event_description = event_description
        self.request_status = request_status
        self.employee_grade = employee_grade
        self.event_grading_type = evemt_grading_type
        self.event_reimbersment = event_reimbersment
        self.event_cost = event_cost
        self.event_location = event_location
        self.event_time = event_time
        self.event_date = event_date
        self.event_type = event_type
        self.employee_id = employee_id
        self.requestid = requestid

    def __repr__(self):
        return str({
            'Request_id': self.requestid,
            'Employee_id': self.employee_id,
            'Event_type': self.event_type,
            'Event_time': self.event_time,
            'Event_date': self.event_date,
            'Event_local': self.event_location,
            'Grade_Type': self.event_grading_type,
            'Employee_grade': self.employee_grade,
            'Event_cost': self.event_cost,
            'Covered_amount': self.event_reimbersment,
            'Event_description': self.event_description,
            'Request_status': self.request_status,
             })

    def json(self):
        return {
                'RequestId': self.requestid,
                'EmployeeId': self.employee_id,
                'EventType': self.event_type,
                'EventTime': str(self.event_time),
                'EventDate': self.event_date,
                'EventLocal': self.event_location,
                'GradeType': self.event_grading_type,
                'EmployeeGrade': self.employee_grade,
                'EventCost': self.event_cost,
                'CoveredAmount': self.event_reimbersment,
                'EventDescription': self.event_description,
                'RequestStatus': self.request_status,
            }
