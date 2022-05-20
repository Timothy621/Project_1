from Models.employee import Employee
from Models.request import Request


def build_request(record):
    return Request(requestid=record[0], employee_id=record[1], event_type=record[2], event_cost=record[3],
                   event_reimbersment=record[4], employee_grade=record[5], request_status=record[6],
                   event_date=record[7], event_time=record[8], event_location=record[9], event_description=record[10],
                   evemt_grading_type=record[11]
                   )


def build_employee(record):
    return Employee(employee_id=record[0], first_name=record[1], last_name=record[2], position=record[3],
                    username=record[4], password=record[5], superviser_code=record[6], departmentid=record[7],
                    )
