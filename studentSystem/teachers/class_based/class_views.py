from ..serializers import StudentSerializer
from ..models import Student

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.http import Http404

class studentData(APIView):
    # Search for students - query
    # only authed persons
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # query_set
    query_set = Student.objects.all()
    
    # search for students    
    def get(self, request):
        id = request.query_params.get('q')
        final = self.query_set.filter(student_id__icontains=id)   
        serialized = StudentSerializer(final, many=True)
        return Response(data=serialized.data, status=200)

# Class_view to edit, delete, search_query, get one student, etc
class StudentObjects(APIView):
    
    # only teachers with tokens are allowed in
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # defns
    model=Student
    serializer = StudentSerializer
    
    # get the student be manipulated - use student id
    def get_student(self, id):
        try:
            return self.model.objects.get(student_id=id)
        except:
            raise Http404 #not found
        
     # add a student
    def post(self, request):
        # check if request.data.id exists
        serialized = self.serializer(data=request.data)
        # validate
        if serialized.is_valid():
            # save
            serialized.save()
            return Response(serialized.data, status=201) #okay
        else:
            return Response(serialized.errors, status=400) #bad request
    
    # edit student details
    def patch(self, request, pk):
        student = self.get_student(pk) #get student. pk is the student id
        serialized = self.serializer(student, data=request.data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(status=200, data='Edited successfully')
        else:
            return Response(serialized.errors, status=400) #bad request
        
    # find single student details
    def get(self, request, pk):
        student= self.get_student(pk)
        # if not found, error raised at get_student. Else serialize
        serialized = self.serializer(student)
        return Response(data=serialized.data, status=200)

    # delete student
    def delete(self, request, pk):
        student = self.get_student(pk)
        student.delete()
        return Response(data='Deleted!', status=204)