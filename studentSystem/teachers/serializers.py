from .models import Teacher, Student;
from rest_framework.serializers import ModelSerializer;


# serialize student data
class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student;
        fields = '__all__';
        
# serialize teacher data
class TeacherSerializer(ModelSerializer):
    class Meta:
        model=Teacher;
        fields=['email', 'isStaff']