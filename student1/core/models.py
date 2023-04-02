from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    pass

class Department(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.name}"

class Teachers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Faculty")

    def __str__(self):
        return f"{self.first_name}"
    
class Standard(models.Model):
    standard = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.standard}"


class Subjects(models.Model):
    subject = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.subject}"
    
class Student(models.Model):
    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField(max_length=254)
    father_name = models.CharField(max_length=254)
    mother_name = models.CharField(max_length=254)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name="kasha", null=True)
    # subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="vishay")


    def __str__(self):
        return f"{self.first_name}"


class Marks(models.Model):
    mark = models.IntegerField()
    # Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="number")
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="vishay")

    def __str__(self):
        return f"{self.subject}: {self.mark}"


class Assignment(models.Model):
    name = models.CharField(max_length=64)
    upload = models.ImageField(upload_to='auctions/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
