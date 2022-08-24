from django.urls import path
from .class_views import studentData, StudentObjects
from .class_views_auth import TeacherDetails, TeacherView

from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

# teachers can:
urlpatterns = [
    # # register
    path('register/', TeacherView.as_view()),
    # # login
    path('login/', TeacherDetails.as_view()),
    
    # add a new student
    path('students/new', StudentObjects.as_view()),
    # get student details
    path('students/get/<str:pk>', StudentObjects.as_view()),
    # update or delete student details
    path('students/edit/<str:pk>',StudentObjects.as_view()),
    # filter students by std id - query params: 'q'
    path('students/search',studentData.as_view()),
]

# for static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)