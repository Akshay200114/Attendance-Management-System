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
    qr_code=models.ImageField(upload_to='qr_codes',blank =True)

    def __str__(self):
        return f"{self.name}   {self.Roll_no}"
    
    def save(self, *args, **kwargs):
        qr_img=qrcode.make(self.Mis_no)
        canvas=Image.new('RGB',(320,320),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qr_img)
        f_name=f'qr_code-{self.name}'+'.png'
        buffer=BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(f_name, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


    class Meta:
        ordering=['Roll_no']


