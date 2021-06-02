from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    mobile=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()


    #models object title change
    def __str__(self):
        return self.name
        