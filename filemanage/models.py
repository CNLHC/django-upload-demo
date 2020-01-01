from django.db import models

class StaticObject(models.Model):
    FileName = models.CharField(max_length=50)
    FileObj =  models.FileField(upload_to='uploads/' )
    Time =  models.DateTimeField(auto_now=True)
    
