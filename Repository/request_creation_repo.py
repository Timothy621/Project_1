from abc import ABC, abstractmethod


class RequestCreationRepo(ABC):

    @abstractmethod
    def create_request(self, request):
        # Method to make new requests
        pass

    @abstractmethod
    def get_employee_request(self, employeeid):
        # Method that gets employee details.
        pass

    @abstractmethod
    def get_request_by_requestid(self, requestid):
        # gets request from requestid
        pass

    @abstractmethod
    def update_request(self, change):
        # update information about request.
        pass

    @abstractmethod
    def close_request(self, clientid):
        # allows client to revoke a request
        pass