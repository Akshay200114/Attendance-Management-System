from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class User(AbstractUser):
    is_teacher = models.BooleanField(null=True)
# Create your models here.

class Student(models.Model):
    name= models.CharField(max_length=64)
    Roll_no=models.PositiveIntegerField()
    Dept=models.CharField(max_length=64)
    Mis_no=models.PositiveIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    sem=models.PositiveIntegerField(null=True)
    qr_code=models.ImageField(upload_to='qr_codes',blank =True)

    def __str__(self):
        return f"{self.name}   {self.Roll_no}"
    
    def save(self, *args, **kwargs):
        qr_img=qrcode.make(self.Mis_no)
        canvas=Image.new('RGB',(320,320),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qr_img)
        f_name=f'{self.name}'+'.png'
        buffer=BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(f_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


    class Meta:
        ordering=['Roll_no']

class Faculty(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    subjects=(
        ["AOS", "Advanced Operating System"],
        ["CN", "Computer Networks"],
        ["WDL","Web Design Lab"],
        ['MP', "Microprocessor"],
        ["DBMS", "DataBase Management System"],
        ["TCS", "Theory Of Computer Science"]
    )
    Subject=models.CharField(max_length=40, choices=subjects)
    Unique_id= models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return f"{self.first_name}"+ ' ' + f"{self.last_name}"

    class Meta:
        ordering=['first_name']

class MarkAttendance(models.Model):
    name=models.CharField(max_length=64)
    roll_no=models.PositiveIntegerField()
    subject=models.CharField(max_length=64)
    Mis_no=models.PositiveIntegerField()
    Department=models.CharField(max_length=64)
    datetime=models.DateTimeField(null= True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} "+ f"{self.subject} "+ f"{self.Department}"

