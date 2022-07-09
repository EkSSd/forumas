from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
        )
from .models import Puslapis, Tagg, Author
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
# from .forms import PostForm
# Create your views here.

class HomeView(ListView):
    model = Puslapis
    template_name = 'home.html'
    ordering = ['-id']


class BlogView(DetailView):
    model = Puslapis
    template_name = "blog_post.html"
    context_object_name = 'post'


class TagView(DetailView):
    model = Tagg
    template_name = 'taggs.html'

class AddPostView(CreateView):
    model = Puslapis
    # form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    fields = '__all__'
   


class UpdatePostView(UpdateView):
    model = Puslapis
    template_name = 'update_post.html'
    success_url = '/'
    fields = ['title', 'tagas', 'content']

def delete_post(request,post_id=None):
    post_to_delete=Puslapis.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect('/')


def authors(request):
    paginator = Paginator(Author.objects.all(), 5)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)


    my_context = {
        "authors": paged_authors,
    }
    return render(request, 'authors.html', context=my_context)

def author(request, author_id):
    single_author = get_object_or_404(Author, id=author_id)
    return render(request, 'author.html',context= {'author': single_author})

















