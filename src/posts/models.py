from django.db import models
from django.urls import reverse

# Create your models here.




class Post(models.Model):
    id = models.AutoField(primary_key=True )
    autor = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
    update = models.DateTimeField(auto_now_add=False, auto_now= True)
    like = models.IntegerField(null=True, default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])


class Comment(models.Model):
    id= models.AutoField(primary_key=True)
    content = models.CharField(max_length=255, null=True)
    autor = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
    like = models.IntegerField(null=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.autor
