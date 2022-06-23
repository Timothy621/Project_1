from Repository.request_aproval_impa import RequestAprovalRepoImpla


class ApprovalService:
    # add filtered request for each level.

    def __init__(self, RequestAprovalRepoImpla:RequestAprovalRepoImpla):
        self.RequestAprovalRepoImpla = RequestAprovalRepoImpla

    def get_all_request(self, approver):
        request_list = []
        if approver["position"] == "BC":
            return self.RequestAprovalRepoImpla.get_all_requests()
        elif approver["position"] == "DH":
            temp_list = self.RequestAprovalRepoImpla.get_all_requests()
            for temp in temp_list:

                check = self.RequestAprovalRepoImpla.department_check(temp.employee_id, approver["department"])
                if check == True:
                    request_list.append(temp)
            return request_list
        elif approver["position"] == "E":
            # need to grab all
            # then sort based on those that have x as y
            temp_list = self.RequestAprovalRepoImpla.get_all_requests()
            for temp in temp_list:
                check = self.RequestAprovalRepoImpla.supervisor_check(approver["employeeID"], temp.employee_id)
                if check == True:
                    request_list.append(temp)
            return request_list

    def approving(self, requestid, approver):
        return self.RequestAprovalRepoImpla.approved(requestid, approver)

    def delete_request(self, requestid):
        return self.RequestAprovalRepoImpla.close_request(requestid)

    def reimburse_adjust(self, change):
        return self.RequestAprovalRepoImpla.adjust_remburse(change)

def test():
    ra = RequestAprovalRepoImpla()
    As = ApprovalService(ra)
    print(f'------BC ------')
    employeeid = "0"
    position = "BC"
    department = "0"
    body = {"employeeID": int(employeeid),
            "position": position,
            "department": int(department)
            }
    print(f'input {body}')
    t = As.get_all_request(body)
    print(t)
    print(type(t[1]))
    print(f'------DH ------')
    employeeid = "1222"
    position = "DH"
    department = "1002"
    body = {"employeeID": int(employeeid),
            "position": position,
            "department": int(department)
            }
    print(f'input {body}')
    t = As.get_all_request(body)
    print(t)
    print(type(t[1]))
    print(f'------Supervisor------')
    employeeid = "9861"
    position = "E"
    department = "1002"
    body = {"employeeID": int(employeeid),
            "position": position,
            "department": int(department)
            }
    print(f'input {body}')
    t = As.get_all_request(body)
    print(t)
    print(type(t[1]))

if __name__ == '__main__':
    test()