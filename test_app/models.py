from django.db import models
from django.utils import timezone
class TestModel(models.Model):
    name=models.CharField(max_length=255,unique=True,null=True,blank=True)
    description =models.TextField()
    phone_number=models.PositiveBigIntegerField()
    is_alive=models.BooleanField()
    amount=models.FloatField()
    extra_name=models.CharField(max_length=255,editable=False, default="null")
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
        

    def __str__(self):
        return f"{self.test_content.test_content.milage}"
    
    class Meta:
        ordering = ("-amount",)
        verbose_name ="Users"
        
    def save(self,*args, **kwargs):
        self.extra_name =f"{self.name} - {self.phone_number}"
        super().save(*args, **kwargs)
        
        
class ModelX(models.Model):
    test_content =models.ForeignKey("TestModel",on_delete=models.CASCADE,related_name="test_content")
    milage=models.FloatField()
    
    def __str__ (self):
        return f"{self.milage}"
    
        class Meta:
            ordering = ("-created_at",)
            verbose_name ="ModelX"
            
            
        
class ModelY(models.Model):
    test_content =models.OneToOneField("TestModel",on_delete=models.CASCADE,related_name="test_content_y")
    milage=models.FloatField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    def __str__ (self):
        return f"{self.test_content.name} - {self.mileage}"
    
        class Meta:
            ordering = ("-created_at",)
            verbose_name ="ModelY"