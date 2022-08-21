from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views, studentViews;

# teachers can:
urlpatterns = [
    # register
    path('register/', views.register),
    # login
    path('login/', views.login),
    
    # add a new student
    path('students/new', studentViews.add_student),
    # get student details
    path('students/get/<str:pk>',studentViews.get_student),
    # update or delete student details
    path('students/edit/<str:pk>',studentViews.edit_student),
    # filter students by std id - query params: 'q'
    path('students/search',studentViews.search_student),
]

# for static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)