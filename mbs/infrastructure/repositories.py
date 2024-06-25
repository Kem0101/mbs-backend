

from mbs.domain.interfaces.repositories import UserRepositoryInterface, ElectoralRollRepositoryInterface
from mbs.domain.entities import User
from .models import User as UserModel, ElectoralRoll as ElectoralRollModel


class UserRepository(UserRepositoryInterface):

    def create(self, user):
        user_model = UserModel.objects.create(
            cedula=user.cedula,
            first_name=user.first_name,
            last_name=user.last_name,
            cell_phone=user.cell_phone,
            email=user.email,
            address=user.address,
            date_born=user.date_born,
            province=user.province,
            electoral_college=user.electoral_college,
            electoral_college_location=user.electoral_college_location,
            role=user.role,
            username=''
        )

        return self._map_user_model_to_domain(user_model)

    def _map_user_model_to_domain(self, user_model):
        user = User(
            id=user_model.id,
            cedula=user_model.cedula,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            cell_phone=user_model.cell_phone,
            email=user_model.email,
            address=user_model.address,
            date_born=user_model.date_born,
            province=user_model.province,
            electoral_college=user_model.electoral_college,
            electoral_college_location=user_model.electoral_college_location,
            role=user_model.role
        )

        return user

    def get_by_cedula(self, cedula):
        try:
            user_model = UserModel.objects.get(cedula=cedula)
            return self._map_user_model_to_domain(user_model)

        except UserModel.DoesNotExist:
            return None


class ElectoralRollRepository(ElectoralRollRepositoryInterface):

    def get_by_cedula(self, cedula):
        try:
            electoral_model = ElectoralRollModel.objects.get(cedula=cedula)
            return electoral_model

        except:
            ElectoralRollModel.DoesNotExist
            return None
