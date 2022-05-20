from Repository.login_repo_impla import LoginRepoImpla

class accountService:
    def __init__(self,  LoginRepoImpla:LoginRepoImpla):
        self.LoginRepoImpla = LoginRepoImpla

    def login(self, username, password):
        return self.LoginRepoImpla.login(username, password)
