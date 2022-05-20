from Repository.request_approval_repo import RequestApprovalRepo
from exceptions.Invalid_transaction import InvalidTransaction
from exceptions.resource_not_found import ResourceNotFound
from util.Dbconnection import connection
from util.builder import build_request, build_employee
from Models.employee import Employee
from Models.request import Request

class RequestAprovalRepoImpla(RequestApprovalRepo):

    def get_all_requests(self, approver):
            sql = "SELECT * FROM request"
            # crates cursor
            cursor = connection.cursor()
            # executes command
            cursor.execute(sql)
            records = cursor.fetchall()
            request_list = [build_request(record) for record in records]
            if request_list:
                return request_list
            else:
                raise ResourceNotFound(f"no requests found")

    def approved(self, requestid, approver):
        sql = "select * from request where requestid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [requestid])
        test = cursor.fetchone()
        test = build_request(test)
        sql = "select * from employees where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [test.employee_id])
        record = cursor.fetchone()
        employee = build_employee(record)
        if test.request_status == "pending super":
            if employee.superviser_code == approver["employeeID"]:
                sql = "UPDATE request Set request_status='pending dh' where requestid= %s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [test.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)
        elif test.request_status == "pending dh":
            if approver["position"] == 'DH' and employee.departmentid == approver["department"]:
                sql = "UPDATE request Set request_status='pending bc' where requestid=%s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [test.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)
        elif test.request_status == "pending bc":
            print("pending BC")
            if approver["position"] == "BC":
                sql = "UPDATE request Set request_status= 'complete' where requestid=%s Returning *"
                cursor = connection.cursor()
                cursor.execute(sql, [test.requestid])
                connection.commit()
                record = cursor.fetchone()
                return build_request(record)

    def adjust_remburse(self, change):
        sql = "select * from request where requestid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [change["requestid"]])
        testid = cursor.fetchone()
        if testid:
            sql = "UPDATE request Set event_reimbersment=%s where requestid = %s Returning *"
            cursor = connection.cursor()
            cursor.execute(sql, [change["amount"], change["requestid"]
                                 ])
            connection.commit()
            record = cursor.fetchone()
            return build_request(record)
        else:
            raise ResourceNotFound(f"request with request id. {change['requestid']} does not exist")

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
        pass


def test():
    ra = RequestAprovalRepoImpla()
    # r =ra.get_request_by_requestid(7314)
    # print(ra.adjust_remburse(r))
    aprover = pull_employee(1222)
    x = ra.get_all_requests(aprover)
    print(x)
    # print(ra.get_request_by_requestid(7314))
    # print("testing aproval of super")
    # aprover = pull_employee(9861)
    # ra.approved(7314, aprover)
    # print(ra.get_request_by_requestid(7314))
    # print("testing aproval of DH")
    # aprover = pull_employee(1222)
    # ra.approved(7314, aprover)
    # print(ra.get_request_by_requestid(7314))
    # print("testing Aproval BC")
    # aprover = pull_employee(1541)
    # print(aprover)
    # ra.approved(7314, aprover)
    # print(ra.get_request_by_requestid(7314))
    # print(ra.get_request_by_employee(237))


def pull_employee(ID):
    sql = "select * from employees where employee_id = %s"
    cursor = connection.cursor()
    cursor.execute(sql, [ID])
    aprover = cursor.fetchone()
    return build_employee(aprover)


if __name__ == '__main__':
    test()
