from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
        )
from django.contrib.auth.models import User
from .models import Post, Tagg 
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PostForm, EditForm
from django.views import generic

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

    


class BlogView(DetailView):
    model = Post
    template_name = "blog_post.html"
    context_object_name = 'post'


class TagView(DetailView):
    model = Tagg
    template_name = 'taggs.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect('/')
        

class AddTaggView(CreateView):
    model = Tagg
    # form_class = PostForm
    template_name = 'add_tag.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
   
class DeleteTaggView(DeleteView):
    model = Tagg
    fields = '__all__'
    template_name = "delete_tag.html"
    success_url = reverse_lazy('home')

class AllTaggView(ListView):
    model = Tagg
    template_name = "all_tags.html"
   




class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = '/'
    # fields = ['title', 'tag', 'content']

def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect('/')


class UserListView(ListView):
    model = User
    template_name = 'authors.html'


def author(request, author_id):
    single_author = get_object_or_404(User, id=author_id)
    return render(request, 'author.html',context= {'author': single_author})

# class AuthorView(DetailView):
#     model = User
#     template_name = "author.html"
#     context_object_name = 'author'












