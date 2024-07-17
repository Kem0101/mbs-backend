

from mbs.domain.entities import User, Coordinator, Facilitator
from mbs.domain.interfaces.repositories import UserRepositoryInterface, ElectoralRollRepositoryInterface


class CreateUser:

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def execute(self, cedula, first_name, last_name, date_born, cell_phone, email, address, province,
                electoral_college, electoral_college_location, role):

        password = self._generate_password(first_name, last_name, cedula)

        user = User(
            cedula=cedula,
            first_name=first_name,
            last_name=last_name,
            date_born=date_born,
            province=province,
            electoral_college=electoral_college,
            electoral_college_location=electoral_college_location,
            cell_phone=cell_phone,
            email=email,
            address=address,
            role=role
        )

        self.user_repository.create(user, password)
        return user

    def _generate_password(self, first_name, last_name, cedula):

        initial_letter_fisrt_name = first_name[0].lower()
        initial_letter_last_name = last_name[0].lower()
        cedula_suffix = cedula[-6:]

        password = f"{initial_letter_fisrt_name}{initial_letter_last_name}{cedula_suffix}"
        return password
