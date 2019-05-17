from django.db import models

# Create your models here.
class stories(models.Model):
    title      = models.CharField(max_length=50,null=False)
    meta_title = models.CharField(max_length=50)
    content    = models.fields.TextField()
    comments   = models.CharField(max_length=500,default="Your thoughts here")
    opinion    = models.BooleanField(default=True,null=False)