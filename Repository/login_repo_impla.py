from Repository.login_repository import LoginRepo
from util.Dbconnection import connection
from util.builder import build_employee


class LoginRepoImpla(LoginRepo):
    def login(self, username, password):
        print("in repo")
        login_status = 'false'
        level = 'none'
        sql = "SELECT * FROM employees where username= %s"
        cursor = connection.cursor()
        # executes command
        cursor.execute(sql, [username])
        record = cursor.fetchone()
        password = str(password)
        if record:
            x = build_employee(record)
            if x:
                print(username)
                if password == x.password:
                    print(password)
                    login_status = 'true'
                    if x.position == "DH":
                        level = 'DH'
                    elif x.position == 'BC':
                        level = 'BC'
                    else:
                        sql = "SELECT * FROM employees where superviser_code = %s"
                        cursor = connection.cursor()
                        # executes command
                        cursor.execute(sql, [x.employee_id])
                        records = cursor.fetchall()
                        if records:
                            level = 'Supervisor'
                    return login_status, level, x
                x = "no object"
                return login_status, level, x
        else:
            x = "no object"
            return login_status, level, x,

def test():
    lr = LoginRepoImpla()
    u = 'SamR'
    p = '1122'
    print(lr.login(u, p))
    u = 'TaraW'
    p = '4321'
    print(lr.login(u, p))
    u = 'JimB'
    p = '1010'
    print(lr.login(u, p))
    u = 'JimB'
    p = 1010
    print(lr.login(u, p))
    u = 'JimB'
    p = '2222'
    print(lr.login(u, p))
    u = 'JdmB'
    p = '2222'
    print(lr.login(u, p))


if __name__ == '__main__':
    test()