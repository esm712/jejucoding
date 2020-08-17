from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    img = models.ImageField()
    dataCreat = models.DateTimeField()
    cateogry = models.CharField(max_length=20)
    
    def __str__(self):#db에title로 저장 
        return self.title 