from django.db import models

# Create your models here.
# class TestModel(models.Model):
    # models.CharField()
    # models.TextField()
    # models.BooleanField()
    # models.oneToManyField()
    # models.ForeignKey()
class TestModel(models.Model):
    name=models.CharField(max_length=255,unique=True,null=True,blank=True)
    description =models.TextField()
    phone_number=models.PositiveBigIntegerField()
    is_live=models.BooleanField()
    amount=models.FloatField()
        
    