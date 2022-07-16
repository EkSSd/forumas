from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

# tevinis modelis

class Tag(models.Model):
    name = models.CharField('tag', max_length=100, unique=True)
    def __str__(self):
            return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    tag = models.ManyToManyField(Tag, related_name='posts')
    content = HTMLField(max_length=20000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True ,null =True)
    post_image = models.ImageField(null=True, blank=True, upload_to='uploads')
    
    def get_absolute_url(self):
        return reverse('blog', args=(str(self.id)))
        # return reverse('home')

    def __str__(self):
        return self.title + ' by ' + str(self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='commenter')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title , self.user)













































