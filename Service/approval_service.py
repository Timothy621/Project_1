from Repository.request_aproval_impa import RequestAprovalRepoImpla


class ApprovalService:
    def __init__(self, RequestAprovalRepoImpla:RequestAprovalRepoImpla):
        self.RequestAprovalRepoImpla = RequestAprovalRepoImpla

    def get_all_request(self, approver):
        return self.RequestAprovalRepoImpla.get_all_requests(approver)

    def approving(self, requestid, approver):
        return self.RequestAprovalRepoImpla.approved(requestid, approver)

    def delete_request(self, requestid):
        return self.RequestAprovalRepoImpla.close_request(requestid)

    def reimburse_adjust(self, change):
        return self.RequestAprovalRepoImpla.adjust_remburse(change)
