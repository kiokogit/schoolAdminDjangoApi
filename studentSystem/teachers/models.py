from django.db import models
from django.contrib.postgres.fields import ArrayField


# teacher model
class Teacher(models.Model):
    # email is also the username
    email = models.EmailField(verbose_name='username', max_length=250,unique=True, blank=False, null=False);
    password = models.CharField(max_length=200, blank=False, null=False);
    # is staff to be signed in token
    isStaff = models.BooleanField(default=True)
    
    USERNAME_FIELD='email';
    
    # str representation
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.email
    
# student data model
class Student(models.Model):
    fname=models.CharField(max_length=200);
    lname=models.CharField(max_length=200);
    student_id = models.CharField(max_length=250, unique=True, blank=False, null=False);
    profile_photo = models.ImageField(upload_to='profiles/')
    activities = ArrayField(models.CharField(max_length=200),blank=True, null=True) 
    
    REQUIRED_FIELDS=['student_id']
    
    def __str__(self):
        return (self.fname + ' ' + self.lname);

