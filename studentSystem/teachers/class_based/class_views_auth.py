from ..models import Teacher
from ..serializers import TeacherSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.http import Http404

class TeacherView(APIView):
    
    model = Teacher
    
    # get teacher object
    def get_teacher(self, email):
        try:
            return self.model.objects.get(email = email)
        except:
            raise Http404
        
    # register user
    def post(self, request):
       
        serialized = TeacherSerializer(data=request.data)
        # validate
        if serialized.is_valid():
            serialized.save()
            return Response(status=201, data=serialized.data) #registered
        else:
            return Response(data=serialized.errors, status=400) #Bad request

class TeacherDetails(TeacherView):
    
    def post(self, request):
        teacher = self.get_teacher(request.data.get('email'))
        # generate token, get_or_create
        token = Token.objects.get_or_create(user=teacher)
        response = Response(data='User Logged in successfully', status=200)
        response['Authentication'] = f'Bearer {token.key}'
        return response