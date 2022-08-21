from django.forms import ModelForm;
from .models import Student, Teacher

# teacher reg form
class teacherRegForm(ModelForm):
    class Meta:
        model = Teacher;
        fields = '__all__'
        
class studentRegForm(ModelForm):
    class Meta:
        model = Student;
        fields = '__all__'