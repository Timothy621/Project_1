import random
from Models.request import Request
from Repository.request_creation_repo import RequestCreationRepo
from exceptions.Invalid_transaction import InvalidTransaction
from exceptions.resource_not_found import ResourceNotFound
from util.Dbconnection import connection
from util.builder import build_request


def _create_id():
    x = random.randint(1, 9999)

    sql = "SELECT requestid FROM request"
    cursor = connection.cursor()
    cursor.execute(sql)
    search = cursor.fetchall()
    if x in search:
        _create_id()
    else:
        return x


def get_event_type(event_type):
    event_type = event_type.lower()
    sql = "SELECT modifier FROM reimbersment Where event_type = %s"
    cursor = connection.cursor()
    cursor.execute(sql, [event_type])
    search = cursor.fetchone()
    return search


class RequestCreationRepoImpl(RequestCreationRepo):
    def create_request(self, request):
        sql = "INSERT INTO request VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *"
        M = get_event_type(request.event_type)
        M = M[0]
        print(M)
        request.requestid = _create_id()
        request.event_cost = int(request.event_cost)
        request.event_reimbersment = request.event_cost * M
        cursor = connection.cursor()
        cursor.execute(sql, [request.requestid, request.employee_id, request.event_type, request.event_cost,
                             request.event_reimbersment, request.employee_grade, request.request_status,
                             request.event_date, request.event_time, request.event_location, request.event_description,
                             request.event_grading_type
                             ])
        connection.commit()
        search = cursor.fetchone()
        return build_request(search)

    def get_employee_request(self, employeeid):
        # stores sql
        sql = "SELECT * FROM request WHERE employee_id = %s"
        # crates cursor
        cursor = connection.cursor()
        # executes command
        cursor.execute(sql, [employeeid])
        records = cursor.fetchall()
        request_list = [build_request(record) for record in records]
        if request_list:
            return request_list
        else:
            raise ResourceNotFound(f"employee {employeeid} has no requests - not found")

    def get_request_by_requestid(self, requestid):
        # stores sql
        sql = "SELECT * FROM request WHERE requestid = %s"
        # crates cursor
        cursor = connection.cursor()
        # executes command
        cursor.execute(sql, [requestid])
        record = cursor.fetchone()
        if record:
            return build_request(record)
        else:
            raise ResourceNotFound(f"request {requestid} - not found")

    def update_request(self, change, update):
        # Update this function To make it so that you do not need all the Info to update.
        # Update Event Time/Date
        # Update Event Location
        # Update Submit Grade

        sql = "select * from request where requestid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [change.requestid])
        testid = cursor.fetchone()
        print(testid)
        if testid:
            if update == "Time/Date":
                print(f'updating + {update}')
                sql = "UPDATE request Set event_date=%s, event_time=%s where requestid = %s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [change.event_date, change.event_time, change.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)
            elif update == "Location":
                print(f'updating + {update}')
                sql = "UPDATE request Set event_location=%s where requestid = %s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [change.event_location, change.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)
            elif update == "Grade":
                print(f'updating + {update}')
                sql = "UPDATE request Set  employee_grade=%s where requestid = %s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [change.employee_grade, change.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)
        #     M = get_event_type(change.event_type)
        #     M = M[0]
        #     print(M)
        #     change.event_cost = int(change.event_cost)
        #     change.event_reimbersment = change.event_cost * M
        #     change.request_status = testid[6]
        #     sql = "UPDATE request Set  event_type=%s, event_cost=%s," \
        #           " employee_grade=%s, event_reimbersment=%s, " \
        #           "event_date=%s, event_time=%s, event_location=%s, event_description=%s, " \
        #           "evemt_grading_type=%s where requestid = %s Returning *"
        #     cursor = connection.cursor()
        #     cursor.execute(sql, [change.event_type, change.event_cost,
        #                          change.employee_grade, change.event_reimbersment,
        #                          change.event_date, change.event_time, change.event_location,
        #                          change.event_description, change.event_grading_type, change.requestid
        #                          ])
        #     connection.commit()
        #     record = cursor.fetchone()
        #     return build_request(record)
        else:
            raise ResourceNotFound(f"request with request id. {change.requestid} does not exist")

    def close_request(self, requestid):
        sql = "select requestid from request where requestid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [requestid])
        testid = cursor.fetchone()

        if testid:
            sql = "select request_status from request where requestid = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [requestid])
            status = cursor.fetchone()
            status = status[0]

            if status == "complete":
                raise InvalidTransaction(f"Employee can't remove request {requestid} because it has"
                                         f" already been completed")
            else:
                sql = "DELETE FROM request WHERE requestid = %s returning *"
                # crates cursor
                cursor = connection.cursor()
                # executes command
                cursor.execute(sql, [requestid])
                connection.commit()
                results = cursor.fetchone()
                return results
        else:
            raise ResourceNotFound(f"request {requestid} does not exist")


