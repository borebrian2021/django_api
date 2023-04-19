from django.db import models
from django.utils import timezone
class TestModel(models.Model):
    name=models.CharField(max_length=255,unique=True,null=True,blank=True)
    description =models.TextField()
    phone_number=models.PositiveBigIntegerField()
    is_alive=models.BooleanField()
    amount=models.FloatField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
        

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%H: %M: %S')} "
    
    class Meta:
        ordering = ("-amount",)