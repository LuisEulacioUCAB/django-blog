from django.db import models
from django.urls import reverse
#from users.models import CustomUser
# Create your models here.
from django.contrib.auth.models import User

def upload_location(instance, filename):
    id = instance
    print(id.autor)
    return "%s/%s" %(instance.id, filename)



class Post(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
    update = models.DateTimeField(auto_now_add=False, auto_now= True)
    like = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='likes', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_location)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.id)])

    @classmethod
    def create(cls, id):
        id = cls(id=id)
        # do something with the book
        return id

class Comment(models.Model):
    id= models.AutoField(primary_key=True)
    content = models.CharField(max_length=255, null=True)
    autor = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now = False)
    like = models.IntegerField(null=True, default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.autor


