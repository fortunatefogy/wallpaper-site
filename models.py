from django.db import models

# Create your models here.



class admins(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

# class walluploadmodel(models.Model):
#     image=models.FileField()
#     imagename=models.CharField(max_length=100)
#     category=models.CharField(max_length=30)
class amoleds(models.Model):
    image=models.FileField(upload_to='wallapp/static/amoled')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)

class darks(models.Model):
    image=models.FileField(upload_to='wallapp/static/dark')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)


class abstracts(models.Model):
    image=models.FileField(upload_to='wallapp/static/abstract')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)


class moviess(models.Model):
    image=models.FileField(upload_to='wallapp/static/movies')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)

class girls(models.Model):
    image=models.FileField(upload_to='wallapp/static/girl')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)

class natures(models.Model):
    image=models.FileField(upload_to='wallapp/static/nature')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)

class animals(models.Model):
    image=models.FileField(upload_to='wallapp/static/animal')
    imagename=models.CharField(max_length=100)
    category=models.CharField(max_length=30)




class uregmodel(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)