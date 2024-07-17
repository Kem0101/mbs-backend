from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model, authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from mbs.infrastructure.repositories import UserRepository, ElectoralRollRepository
from mbs.application.use_cases.create_user import CreateUser
from mbs.infrastructure.models import CustomUser


import json

# Create your views here.
CustomUser = get_user_model()


def index(request):
    return HttpResponse('Hola mundo!')


@method_decorator(csrf_exempt, name='dispatch')
class CedulaValidateView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.electoral_roll_repository = ElectoralRollRepository()

    def get(self, request):
        cedula = request.GET.get('cedula')

        if not cedula:
            return JsonResponse({'error': 'Cedula is required'}, status=400)

        try:
            electoral_data = self.electoral_roll_repository.get_by_cedula(
                cedula)
            if electoral_data:
                return JsonResponse({
                    'cedula': electoral_data.cedula,
                    'first_name': electoral_data.first_name,
                    'last_name': electoral_data.last_name,
                    'date_born': electoral_data.date_born,
                    'province': electoral_data.province,
                    'electoral_college': electoral_data.electoral_college,
                    'electoral_college_location': electoral_data.electoral_college_location
                }, status=200)
            else:
                return JsonResponse({'error': 'Cedula not found in electoral database'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_repository = UserRepository()

    def post(self, request):
        data = json.loads(request.body)

        cedula = data.get('cedula')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_born = data.get('date_born')
        cell_phone = data.get('cell_phone')
        address = data.get('address')
        province = data.get('province')
        electoral_college = data.get('electoral_college')
        electoral_college_location = data.get('electoral_college_location')
        role = data.get('role')

        if not all([cedula, first_name, last_name, date_born, cell_phone, address, province, electoral_college, electoral_college_location, role]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        try:
            create_user_use_case = CreateUser(self.user_repository)
            user = create_user_use_case.execute(
                cedula=cedula,
                first_name=first_name,
                last_name=last_name,
                date_born=date_born,
                cell_phone=cell_phone,
                email=data.get('email', ''),
                address=address,
                province=province,
                electoral_college=electoral_college,
                electoral_college_location=electoral_college_location,
                role=role
            )
            return JsonResponse({'message': 'User created successfully'}, status=201)

        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        cedula = request.data.get('cedula')
        password = request.data.get('password')

        if not cedula or not password:
            return Response({'error': 'Cedula and password are required'}, status=400)

        user = authenticate(request, cedula=cedula, password=password)
        print(user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
