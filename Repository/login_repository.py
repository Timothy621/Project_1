from abc import ABC, abstractmethod


class LoginRepo(ABC):
    @abstractmethod
    def login(self, username, password):
        # Method that gets employee details.
        pass
