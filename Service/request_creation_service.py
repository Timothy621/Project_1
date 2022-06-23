from Repository.request_creation_imple import RequestCreationRepoImpl


class RequestService:
    def __init__(self, RequestCreationRepoImpl: RequestCreationRepoImpl ):
        self.RequestCreationRepoImpl = RequestCreationRepoImpl

    def create_request(self, request):
        return self.RequestCreationRepoImpl.create_request(request)

    def get_request(self, requestid):
        return self.RequestCreationRepoImpl.get_request_by_requestid(requestid)

    def get_all_request_of_employee(self, employeeid):
        return self.RequestCreationRepoImpl.get_employee_request(employeeid)

    def update_request(self, Change, update):
        return self.RequestCreationRepoImpl.update_request(Change, update)

    def delete_request(self,requestid):
        return self.RequestCreationRepoImpl.close_request(requestid)
