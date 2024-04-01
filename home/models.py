from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True,blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
