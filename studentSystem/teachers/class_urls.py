from django.urls import path
from .class_views import studentData, StudentObjects
from .class_views_auth import TeacherDetails, TeacherView

from django.conf import settings
from django.conf.urls.static import static

# teachers can:
urlpatterns = [
    # # register
    path('register/', TeacherView.as_view()),
    # # login
    path('login/', TeacherDetails.as_view()),
    
    # add a new student
    path('students/new', studentData.as_view()),
    # get student details
    path('students/get/<str:pk>', studentData.as_view()),
    # update or delete student details
    path('students/edit/<str:pk>',StudentObjects.as_view),
    # filter students by std id - query params: 'q'
    # path('students/search',studentViews.search_student),
]

# for static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)