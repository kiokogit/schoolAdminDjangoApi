from django.db import models

# Create your models here.
# teacher model
class Teacher(models.Model):
    # email is also the username
    email = models.EmailField(verbose_name='username', max_length=250,unique=True, blank=False, null=False);
    password = models.CharField(max_length=200, blank=False, null=False);
    id_no = models.CharField(max_length=200, blank=False, null=False);
    # is staff to be signed in token
    isStaff = models.BooleanField(default=True)
    
    '''# return isStaff - true
    def isStaff():
        return True
     '''
     
    