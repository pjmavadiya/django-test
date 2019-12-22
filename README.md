# django-test
Create a backend application allowing management of schools and students

Create a backend application allowing management of schools and students

Keep track of the time you spend on each part of this project and send it with your submission to [yassine.belmamoun@manatal.com](mailto:yassine.belmamoun@manatal.com).


# Step 1    [Completed]


- Create a Django app, with Postgres as a database, and Pipenv as a Python dependency manager. (We recommend using a Ubuntu system)

- Add models to create the following structure:

  - Students have a first name, a last name, and a student identification string (20 characters max for each)
  - Schools have a name (20 char max) and a maximum number of student (any positive integer)
  - Each student object must belong to a school object


# Step 2    [Completed]

This second step focuses on Django Rest Framework (DRF).

- Add Django REST framework library to your project by using Pipenv

- Feel free to use the DRF browsable API for testing things manually.

- Design your API according to specifications below. You can use ModelViewSet and ModelSerializer to automatically handle the different API HTTP methods:
https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
And make sure to test and customize if any customization is needed. Knowing that, create urls, views, serializers for all your models so that:
  - endpoint /students/ will return all students (GET) and allow student creation (POST)
  - endpoint /schools/ will return all schools (GET) and allow school creation (POST)
  - endpoint /schools/:id and /students/:id will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
  - student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
  - trying to add a student in a full school (maximum number of student reached) will return a DRF error message


# Step 3    [Completed]

This third step focuses on Django Nested Routers.

- Add Django Nested Routers library to your project by using Pipenv

- Design your API according to specifications below. You can use ModelViewSet and ModelSerializer to automatically handle the 
different API HTTP methods, and test and customize if any customization is needed. Knowing that, create urls, views, serializers for all your models so that:
  - endpoint /schools/:id/students will return students who belong to school :id (GET)
  - endpoint /schools/:id/students will allow student creation in the school :id (POST)
  - your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
  - your nested endpoint will respect the same two last rules of Step 2 too


# Bonus     [Completed]

- You can add fields of your choice to students and schools such as location, nationality, age, etc. You can use Python Faker library to generate random data (names, etc) to populate fields.

- You can add search filters to your endpoints such as /students/?search=alex and you can add ordering filters as well, for example by age, by nationality, etc.

- You can add pagination or anything else that you wanna show us, feel free to add interesting stuff to this project!


# Guidelines

- Send us the project and your comments as a git patch or repository, or a hosted live demo