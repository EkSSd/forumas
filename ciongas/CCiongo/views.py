from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Puslapis, Tagg, Author
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .forms import PostForm
# Create your views here.

class HomeView(ListView):
    model = Puslapis
    template_name = 'home.html'


class BlogView(DetailView):
    model = Puslapis
    template_name = "blog_post.html"
    context_object_name = 'post'


class TagView(DetailView):
    model = Tagg
    template_name = 'taggs.html'

class AddPostView(CreateView):
    model = Puslapis
    form_class = PostForm
    template_name = 'add_post.html'
    fields = '__all__'
   



def authors(request):
    paginator = Paginator(Author.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)


    my_context = {
        "authors": paged_authors,
    }
    return render(request, 'authors.html', context=my_context)

def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html',context= {'author': single_author})

















