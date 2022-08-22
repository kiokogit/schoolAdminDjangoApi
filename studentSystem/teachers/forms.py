from django.forms import ModelForm;
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Teacher

# teacher reg form
class teacherRegForm(UserCreationForm):
    class Meta:
        model = Teacher;
        fields = ['email', 'password1', 'password2']
        
class studentRegForm(ModelForm):
    class Meta:
        model = Student;
        fields = '__all__'