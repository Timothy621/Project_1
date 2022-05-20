from flask import jsonify, request
from Models.employee import Employee
from Service.account_service import accountService
from exceptions.resource_not_found import ResourceNotFound
from Repository.login_repo_impla import LoginRepoImpla
lr = LoginRepoImpla()
As = accountService(lr)

def route(app):
    @app.route("/login/<username>/<password>", methods=["GET"])
    def login(username, password):
        print("in login controller")
        x = As.login(username, password)
        if x[2] == "no object":
            C = {'LoginStatus': x[0],
                 'Level': x[1],
                 'employee': 'not found'
                 }
        else:
            C = {'LoginStatus': x[0],
                 'Level': x[1],
                 'employee': x[2].json()
                 }
            print("Exit Controller")
        return jsonify(C)

