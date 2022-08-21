# schoolAdminDjangoApi
<!-- to solve a django project interview question by geoProject -->

## Introduction
This app contains a list of students in a school with activites that they can participate in.

## DATABASE
Edit settings.py for db
'Students Activities' requires ArrayField, supported in psgsql, not dbsqlite3

Alternative would be to have a ManyToManyRel btn Student and Activities models

## Auth
Uses django-rest token models and auth classes

# EXPOSED ENDPOINTS
admin: 'admin/'

user:
```py
## register as a user(teacher)

'api/register

required: {email, password1, password2}

## login
'api/login
required: {email, password}

## add a new student
'api/students/new'
required: {fname, lname, student_id(unique)}
optional: {activities:[], profile_photo}

## get student details
'api/students/get/<str:pk>'
required: {pk=student_id}

## search for students
'api/students/search'
required: search_params in form of {q=''}

## patch/delete student records
'api/students/edit/<str:pk>
required: student_id
```

# GETTING STARTED
install dependencies in requirements.txt

$ pip install -r requirements.txt

then run the server once all dependencies are installed
$ python manage.py runserver

THANK YOU
