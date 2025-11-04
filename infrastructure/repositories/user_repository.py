class UserRepository:
    def __init__(self):
        self._users = []

    def save(self, user):
        self._users.append(user)

    def list_all(self):
        return self._users