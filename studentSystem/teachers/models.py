from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


# teacher model, abstract user
class Teacher(AbstractUser):
    isStaff=models.BooleanField(default=True)
    email=models.EmailField(max_length=250, unique=True)
    # str representation
    def __str__(self):
        return self.email
    
# student data model
class Student(models.Model):
    fname=models.CharField(max_length=200);
    lname=models.CharField(max_length=200);
    student_id = models.CharField(max_length=250, unique=True, blank=False, null=False);
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True);
    activities = ArrayField(models.CharField(max_length=200),blank=True, null=True);

    
    def __str__(self):
        return (self.fname + ' ' + self.lname);

