import json
from flask import jsonify, request
from Models.employee import Employee
from Models.request import Request
from exceptions.resource_not_found import ResourceNotFound
from Repository.request_aproval_impa import RequestAprovalRepoImpla
from Service.approval_service import ApprovalService
rar = RequestAprovalRepoImpla()
As = ApprovalService(rar)


def route(app):

    @app.route("/employee/request/<employeeid>/<position>/<department>", methods=["GET"])
    def get_all_employees(employeeid, position, department):
        body = {"employeeID": int(employeeid),
                "position": position,
                "department": int(department)
                }
        print(body)
        try:
            return jsonify([Request.json() for Request in As.get_all_request(body)]), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/request/<requestid>/<employeeid>/<position>/<department>", methods=["PUT"])
    def approve_request(requestid, employeeid, position, department):
        body = {"employeeID": int(employeeid),
                "position": position,
                "department": int(department)
                }
        print(body)
        txt = As.approving(requestid, body)
        print(txt)
        return txt.json()

    @app.route("/employee/request/adjust/<requestid>/<amount>", methods=["put"])
    def adjust_reimburse(amount, requestid):
        body = {
            "amount": amount,
            "requestid": requestid
        }
        try:
            x = As.reimburse_adjust(body).json()
            print(x)
            print(type(x))
            return x
        except ResourceNotFound as r:
            return r.message, 404
