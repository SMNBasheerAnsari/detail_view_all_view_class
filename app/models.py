from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sc_name=models.CharField(max_length=100)
    sc_principal=models.CharField(max_length=100)
    sc_location=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.sc_name
    

class Student(models.Model):
    st_name=models.CharField(max_length=100)
    st_age=models.IntegerField()
    sc_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='pandas')
    #related_name=fetching data of child table without using child table but with the help of parent table object
    
    def __str__(self):
        return self.st_name
