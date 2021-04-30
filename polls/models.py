from django.db import models

# Create your models here.
#คำถามกับตัวเลือก
class Questions(models.Model):
    question = models.CharField(max_lenght = 250 )
    pub_date = models.DateTimeField('datepublished')

class Choice(models.Model):
    choice = models.CharField(max_lenght = 250 )
    