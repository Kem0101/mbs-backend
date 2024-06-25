from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from mbs.application.use_cases.create_user import CreateUser
from mbs.infrastructure.repositories import UserRepository, ElectoralRollRepository


# Create your views here.

def index(request):
    return HttpResponse('Hola mundo!')


@method_decorator(csrf_exempt, name='dispatch')
class UserRepositoryView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_repository = UserRepository()
        user_roll_repository = ElectoralRollRepository()
        self.create_user_use_case = CreateUser(
            user_repository, user_roll_repository)

    def post(self, request):
        data = json.loads(request.body)
        cedula = data['cedula']
        cell_phone = data['cell_phone']
        email = data['email']
        address = data['address']
        role = data['role']

        try:
            user = self.create_user_use_case.execute(
                cedula, cell_phone, email, address, role)
            return JsonResponse({
                'id': user.id,
                'cedula': user.cedula,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_born': user.date_born,
                'province': user.province,
                'electoral_college': user.electoral_college,
                'electoral_college_location': user.electoral_college_location
            })
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
