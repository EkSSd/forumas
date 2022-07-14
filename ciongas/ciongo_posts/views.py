from django.shortcuts import render, get_object_or_404, redirect
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
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    # form_class = TagForm
    template_name = 'add_tag.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    
    # @method_decorator(login_required)
    # def dispatch(self, request):
    #     edit = self.get_object()
    #     if edit and not edit.name == self.request.user:
    #         messages.error(
    #             self.request,
    #             'You are not allowed to access this page'
    #         )
    #         return HttpResponseRedirect('/')
    #     return super(AddTaggView, self).dispatch(request)

class AllTaggView(ListView):
    model = Tagg
    template_name = "all_tags.html"
   




class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = '/'
    # fields = ['title', 'tag', 'content']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        edit = self.get_object()
        if edit and not edit.author == self.request.user:
            messages.error(
                self.request,
                'You are not allowed to access this page'
            )
            return HttpResponseRedirect('/')
        return super(UpdatePostView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='/accounts/login/')
def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login/')
def delete_tag(request, tag_id=None):
    data = Tagg.objects.get( id=tag_id) 
    # remmo_post = Post()
    data.delete()
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













