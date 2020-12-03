from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(null=True)
# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=64)
    Roll_no=models.PositiveIntegerField()
    Dept=models.CharField(max_length=64)
    Mis_no=models.PositiveIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}   {self.Roll_no}"

    class Meta:
        ordering=['Roll_no']


