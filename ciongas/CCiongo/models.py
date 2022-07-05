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



class Puslapis(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    tagas = models.ManyToManyField(Tagg, related_name='posts')
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True ,null =True)

    # def display_tag(self):
    #     return ','.join(tag.name for tag in self.tag.all()[:3])' # cia keiciau ne syky bet taip ir palikau kol sugalvosiu
    def get_absolute_url(self):
        return reverse('blog', args=(str(self.id)))

    def __str__(self):
        return self.title + ' by ' + str(self.author)



class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)
    # description = models.TextField('aprasymas', max_length=2000, default='')
    description = HTMLField()

    # def display_books(self):
    #     return ', '.join(book.title for book in self.books.all())

    # display_books.short_description = 'books'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'















































