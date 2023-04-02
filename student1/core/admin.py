from django.contrib import admin

from .models import User, Department, Teachers, Student, Standard, Subjects, Marks, Assignment

# Register your models here.
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Teachers)
admin.site.register(Student)
admin.site.register(Standard)
admin.site.register(Subjects)
admin.site.register(Marks)
admin.site.register(Assignment)