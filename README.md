<!-- to solve a django project interview question by geoProject -->

### Introduction
This app contains a list of students in a school with activites that they can participate in.

### DATABASE
Edit <settings.py> for db

'Students Activities' requires ArrayField, supported in psgsql, not dbsqlite3

Alternative would be to have a ManyToManyRel btn Student and Activities models

### Auth
Uses django-rest token models and auth classes

### EXPOSED ENDPOINTS
admin: 'admin/'

user:
```py
## register as a user(teacher)

'api/fns/register
'api/cls/register

required: {email, password1, password2}

## login
'api/fns/login
'api/cls/login
required: {email, password}

## add a new student
'api/fns/students/new'
'api/cls/students/new'
required: {fname, lname, student_id(unique)}
optional: {activities:[], profile_photo}

## get student details
'api/fns/students/get/<str:pk>'
'api/cls/students/get/<str:pk>'
required: {pk=student_id}

## search for students
'api/fns/students/search'
'api/cls/students/search'
required: search_params in form of {q=''}

## patch/delete student records
'api/fns/students/edit/<str:pk>
'api/cls/students/edit/<str:pk>
required: student_id
```

## GETTING STARTED
install dependencies in requirements.txt

$ pip install -r requirements.txt

then run the server once all dependencies are installed

$ cd studentSystem

$ python manage.py runserver

### Notices
For development only:

1. csrf cookie middleware has been disabled
2. Token authentication format: headers['Authorization'] = 'Token [key]'
3. All origins allowed
4. Any host allowed

THANK YOU
