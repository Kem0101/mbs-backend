

class UserRepositoryInterface:

    def create(self, user, password):
        raise NotImplementedError

    def get_by_cedula(self, cedula):
        raise NotImplementedError


class ElectoralRollRepositoryInterface:

    def get_by_cedula(self, cedula):
        raise NotImplementedError
