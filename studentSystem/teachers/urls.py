from django.urls import path

# teachers can:
urlpatterns = [
    # register as a teacher
    path('register/', name='register'),
    # login as a teacher
    path('login/', name='login'),
    
    # add a new student
    path('student/new', name='new_student'),
    # view student details
    path('students/<str>:id', name='view_student'),
    # change student details
    path('students/id', name='update_student'),
    # delete student
    path('student/id', name='del_student'),
    # filter students by id
    path('students/search?', name='search_student'),
]