from django.shortcuts import render

# import rest framework decorators, response
from rest_framework.decorators import api_view;
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate


from .forms import teacherRegForm
from .models import Teacher;

# Create your views here.

# register as a teacher
@api_view(['POST'])
def register(request):
    form = teacherRegForm()
    # contains email, password
    rawData = request.data;
    email = rawData['email']
    password = rawData['password'];
    
    # check if user exists
    try:
        # if not found, raises an exception, hence proceeds. else, return bad request
        Teacher.objects.get(email=email)
        return Response(status=400, data='User already exists')
    except:
        # populate form
        form = teacherRegForm({'email':email, 'password':password});
        # validate form, save, return created
        if form.is_valid():
            form.save(commit=True);
            
            return Response(status=201, data='User created successfully')
        
        # else log out errors, and return bad request
        else:
            print(form.errors.as_json)
            return Response(status=400, data='Invalid request') #bad request
        

# Login as a teacher
@api_view(['POST'])
def login(request):
    
    rawData = request.data
    email = rawData['email']
    password = rawData['password']
    
    # validate request data, and check if user exists
    try:
        Teacher.objects.get(email=email)
        # throws an exception if user does not exist
    except :
        # exception terminates
        return Response(status=401) #invalid email
    
    # else: authenticate using authenticate(). returns email if true, else None
    user = authenticate(email=email, password=password)
    if user is None:
        # invalid password
        return Response(status=403) #invalid password.
    else:
        # generate token, and send as a bearer token
        token = Token.create(user=user)
        
    
    return Response(data='')