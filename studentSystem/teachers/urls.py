from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views, studentViews;

# teachers can:
urlpatterns = [
    # register
    path('register/', views.register, name='register'),
    # login
    path('login/', views.login, name='login'),
    
    # add a new student
    path('student/new', studentViews.add_student, name='new_student'),
    # get student details
    path('students/get/<str:id>',studentViews.get_student, name='get_student'),
    # update or delete student details
    path('students/<str:id>',studentViews.edit_student, name='update_student'),
    # filter students by id
    path('students/search?<id>',studentViews.search_student, name='search_student'),
]

# for static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)