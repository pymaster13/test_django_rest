# Test Task Django Rest Framework
This project (task) is an API to represent the company structure. It was design for 2 work days.

## Getting Started
Python version: 3.8.10

Clone project:
```
git clone https://github.com/pymaster13/test_django_rest.git && cd test_django_rest
```

Create and activate virtual environment:
```
python3 -m venv venv && source venv/bin/activate
```

Install libraries:
```
python3 -m pip install -r requirements.txt
```

Run local Django server:
```
python3 manage.py runserver
```

## Task Description

##### <a name="Emphasis"></a>To develop:
* List of departments
* List of employees (both general and by department separately)

##### <a name="Emphasis"></a>Data model:

The employee contains the attributes:

* Full name
* Photo
* Position
* Salary
* Age
* Department

The department contains:

* Name
* Communication with an employee - director of the department

The uniqueness of the “employee-department” link must be ensured.

The search query by employee's last name should be optimized.
admin

An admin panel should be implemented in which you can look at these models and modify them.

##### <a name="Emphasis"></a>REST API

* API for getting a list of employees + implement a filter for searching by last name and department id
* Adding/removing employees via API
* API for getting a list of departments (includes an artificial field with the number of employees + a field with total salaries for all employees)
* API with a list of employees - with pagination, API with a list of departments - without pagination
* Access to the list of employees - only for authorized users, access to the list of departments - is also available for anonymous users

##### <a name="Emphasis"></a>Expected Result

* A set of API methods for working with data on employees and departments
* Swagger documentation on API methods
* Admin by data model 

### Features

Main libraries that are used : 
* Django 3,
* djangorestframework,
* djangorestframework-simplejwt,
* django-rest-swagger (drf-spectacular).
