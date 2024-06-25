

from mbs.domain.entities import User, Coordinator, Facilitator
from mbs.domain.interfaces.repositories import UserRepositoryInterface, ElectoralRollRepositoryInterface


class CreateUser:

    def __init__(self, user_repository: UserRepositoryInterface, electoral_roll_repository: ElectoralRollRepositoryInterface):
        self.user_repository = user_repository
        self.electoral_roll_repository = electoral_roll_repository

    def execute(self, cedula, cell_phone, email, address, role):
        electoral_data = self.electoral_roll_repository.get_by_cedula(cedula)
        if not electoral_data:
            raise ValueError('Cedula no encontrada en el padron electoral')

        user = User(
            cedula=cedula,
            first_name=electoral_data.first_name,
            last_name=electoral_data.last_name,
            date_born=electoral_data.date_born,
            province=electoral_data.province,
            electoral_college=electoral_data.electoral_college,
            electoral_college_location=electoral_data.electoral_college_location,
            cell_phone=cell_phone,
            email=email,
            address=address,
            role=role
        )

        self.user_repository.create(user)
        return user
