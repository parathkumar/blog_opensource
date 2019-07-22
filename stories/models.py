from django.db import models
# Create your models here.
class stories(models.Model):
    title      = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=50)
    content    = models.TextField(max_length=100000)
    comments   = models.CharField(max_length=500,default="Your thoughts here")
    #opinion    = models.BooleanField(default=True,null=False)
    picture    = models.ImageField(upload_to="pictures/",default="/pictures/pict.jpg")
    author     = models.CharField(max_length=100,null=False,default="guest",)
    def __str__(self):
        return self.title

class Rating(models.Model):
    blog_point = models.ForeignKey(stories , on_delete=models.CASCADE)
    rank       = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.rank)