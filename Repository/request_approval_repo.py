from abc import ABC, abstractmethod


class RequestApprovalRepo(ABC):
    @abstractmethod
    def get_all_requests(self,):
        # Method that gets employee details.
        pass

    @abstractmethod
    def approved(self, requestid, approver):
        pass

    @abstractmethod
    def adjust_remburse(self, change):
        # update information about request.
        pass

    @abstractmethod
    def close_request(self, requestid):
        # allows
        pass
