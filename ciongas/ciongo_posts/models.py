from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

# tevinis modelis

class Tagg(models.Model):
    name = models.CharField('tagg', max_length=100)
    def __str__(self):
            return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tag = models.ManyToManyField(Tagg, related_name='posts')
    content = HTMLField(max_length=20000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True ,null =True)

    
    def get_absolute_url(self):
        return reverse('blog', args=(str(self.id)))
        # return reverse('home')

    def __str__(self):
        return self.title + ' by ' + str(self.author)


 
















































