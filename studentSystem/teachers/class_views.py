from .serializers import StudentSerializer
from .models import Student

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


class studentData(APIView):
    # List all students
    authentication_classes=[TokenAuthentication]
    
    # get all Students
    def get(self, request):
        
        student = Student.objects.all()
        serialized = StudentSerializer(data=student)
        return Response(serialized.data, status=200)
    
    # add a student
    def post(self, request):
        # check if request.data.id exists
        serialized = StudentSerializer(data=request.data)
        # validate
        if serialized.is_valid():
            # save
            serialized.save()
            return Response(serialized.data, status=201) #okay
        else:
            return Response(serialized.errors, status=400) #bad request

# Class_view to edit, delete, search_query, get one student, etc
class StudentObjects(APIView):
    
    # only teahcers with tokens are allowed in
    authentication_classes=[TokenAuthentication]
    
    # get the student be manipulated
    def get_student(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except:
            return 'NotFound';
        
    # edit student details
    def patch(self, request, pk):
        student = self.get_student(pk)
        serialized = StudentSerializer(student, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data='Edited successfully')
        else:
            return Response(serialized.errors, status=400)