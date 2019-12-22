from django.db import models


class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.IntegerField()
    state = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, related_name="school", on_delete="CASCADE")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    s_id = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    nationality = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

