from django.contrib import admin
from .models import *


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_student',)
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'school', )


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)