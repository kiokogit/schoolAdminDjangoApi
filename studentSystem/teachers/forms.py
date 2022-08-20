from django.forms import ModelForm;
from .models import Teacher

# teacher reg form
class teacherRegForm(ModelForm):
    class Meta:
        model = Teacher;
        fields = '__all__'