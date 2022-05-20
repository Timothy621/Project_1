
class Department:
    def __init__(self,departmentid, department_name, department_head_id):
        self.department_head_id = department_head_id
        self.department_name = department_name
        self.departmentid = departmentid

    def __repr__(self):
        str({
            'departmentid': self.departmentid,
            'department_name': self.department_name,
            'department_head_id': self.department_head_id
        })

    def json(self):
        return {
            'departmentId': self.departmentid,
            'departmentName': self.department_name,
            'departmentHeadId': self.department_head_id
        }
