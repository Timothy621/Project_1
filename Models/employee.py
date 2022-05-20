class Employee:
    def __init__(self, employee_id =0, first_name="NoName", last_name="NoName", position="E", username="Nousername", password=1111, superviser_code=1111, departmentid=1111):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.username = username
        self.password = password
        self.superviser_code = superviser_code
        self.departmentid = departmentid

    def __repr__(self):
        return str({
            'employee_id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'position': self.position,
            'username': self.username,
            'password': self.password,
            'superviser_code': self.superviser_code,
            'departmentid': self.departmentid
        })

    def json(self):
        return {'employeeId': self.employee_id,
                'firstName': self.first_name,
                'lastName': self.last_name,
                'position': self.position,
                'username': self.username,
                'password': self.password,
                'superviserCode': self.superviser_code,
                'departmentId': self.departmentid
                }
