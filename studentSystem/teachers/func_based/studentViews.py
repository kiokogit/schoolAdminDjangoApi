from ..forms import studentRegForm
from ..serializers import StudentSerializer
from ..models import Student;

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# add a new student
@api_view(['POST', 'OPTIONS'])
@authentication_classes([TokenAuthentication]) # adds request.user as user object
def add_student(request):

    form = studentRegForm(request.data)
    if form.is_valid():
        form.save(commit=True);
        return Response(status=201, data='Student registered Successfully') #new student created successfully
    else:
        # log out errors - use an app logger, return bad request
        print(form.errors.as_json)
        return Response(status=400, data='Bad Request. Student Exists') #bad request
    
# UPDATE, DEL ONE STUDENT
@api_view(['PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
def edit_student(request, pk):
    
    # check if student exists
    editedData = request.data
    student = Student.objects.get(student_id=pk) #id -the student id
    if student is None:
        return Response(status=404) #Student notFound
    if request.method=='PATCH':
        # user may send only the portion of the object to be edited
        form = studentRegForm(editedData, instance=student)
        if form.is_valid():
            form.save(commit=True);
            
            # return the new object, serialized
            finalData = Student.objects.get(student_id=pk) #id the primary key
            serialized = StudentSerializer(finalData, many=False);
            return Response(status=201, data=serialized.data)
            
    # deleting
    elif request.method=='DELETE':
        # use try except to alert if not deleted
        try:
            student.delete();  
            return Response(status=200, data=f'Student of id {pk} successfully deleted from records') #All is well
        except:
            # log out errors
            return Response(status=500) #Something went wrong
        
        
# GET DETAILS OF ONE STUDENT - Not protected by token
@api_view(['GET','OPTIONS'])
def get_student(request, pk):
    
    try:
        student = Student.objects.get(student_id=pk)
        # serialize
        serialized = StudentSerializer(student, many=False)
        return Response(status=200, data=serialized.data) #All is well
    except:
        # user not found
        return Response(status=404) #notFound


# FILTER STUDENT USING ID - SEARCH USER
@api_view(['GET', 'OPTIONS'])
def search_student(request):
    # get req.query
    try:
        id = request.query_params.get('q')

        # use icontains to query all parts of the student id
        students = Student.objects.all().filter(student_id__icontains=id)
        # serialize
        serialized = (StudentSerializer(students, many=True))
        if len(serialized.data)==0:
            return Response(status=404, data='Not found') #not found
        
        return Response(status=200, data=serialized.data)
    except:
    # not found
        return Response(status=500) #Error occured
