from flask import jsonify, request
from Repository.request_creation_imple import RequestCreationRepoImpl
from Service.request_creation_service import RequestService
from exceptions.Invalid_transaction import InvalidTransaction
from exceptions.resource_not_found import ResourceNotFound
from Models.request import Request
rcr = RequestCreationRepoImpl()
rs = RequestService(rcr)


def route(app):

    @app.route("/employee/<employeeid>/request", methods=["GET"])
    def get_request_from_employee(employeeid):
        try:
            return jsonify([Request.json() for Request in rs.get_all_request_of_employee(employeeid)]), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employeeid>/request/<requestid>", methods=['GET'])
    def get_request_by_id(employeeid, requestid):
        x = employeeid
        try:
            return rs.get_request(int(requestid)).json(), 200
        except ValueError as e:
            return e, 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employeeid>/request/", methods=["POST"])
    def post_request(employeeid):
        body = request.json

        temp = Request(requestid=body["requestid"], employee_id=employeeid, event_type=body["eventType"],
                       event_date=body["eventDate"], event_time=body["eventTime"], event_location=body["eventLocation"],
                       event_cost=body["eventCost"], event_reimbersment=body["eventReimbersment"],
                       evemt_grading_type=body["eventGradingType"], employee_grade="N/A",
                       request_status=body["requestStatus"], event_description=body["eventDescription"],)
        try:
            temp = rs.create_request(temp)
        except ValueError as e:
            return e, 400
        return temp.json(), 201

    @app.route("/employee/<employeeid>/request/<requestid>", methods=["PUT"])
    def update_request(employeeid, requestid):
        body = request.json
        temp = Request(requestid=int(requestid), employee_id=int(employeeid), event_type=body["eventType"],
                       event_date=body["eventDate"], event_time=body["eventTime"], event_location=body["eventLocation"],
                       event_cost=body["eventCost"], event_reimbersment=body["eventReimbersment"],
                       evemt_grading_type=body["eventGradingType"], employee_grade=body["employeeGrade"],
                       request_status=body["requestStatus"], event_description=body["eventDescription"],)
        try:
            return jsonify(rs.update_request(temp).json())
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employeeid>/request/<requestid>", methods=["DELETE"])
    def delete_request(employeeid,requestid):
        e = employeeid
        try:
            rs.delete_request(requestid)
        except ResourceNotFound as r:
            return r.message, 404
        except InvalidTransaction as i:
            return i.message, 422
        return '', 204  # No Content
