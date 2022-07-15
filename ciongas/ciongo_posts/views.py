from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
        )
from django.contrib.auth.models import User
from .models import Post, Tag
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PostForm, EditForm
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required

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
    model = Tag
    template_name = 'taggs.html'

class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    # fields = '__all__'

    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect('/')

    
            

class AddTaggView(CreateView):
    model = Tag
    # form_class = TagForm
    template_name = 'add_tag.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    # def no_duplicates( request):
    #     for na in Tagg.objects.all():
    #         if na.name == na.name:
    #             return HttpResponseRedirect('addtag')

class AllTaggView(ListView):
    model = Tag
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
        if edit.author != request.user:
            raise Http404()
        if edit and not edit.author == self.request.user:
            messages.error(
                self.request,
                'You are not allowed to access this page'
            )
            return HttpResponseRedirect('/')
        return super(UpdatePostView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='login')
def delete_post(request,post_id=None):
    post_to_delete=get_object_or_404(Post, id=post_id)
    if post_to_delete.author != request.user:
        raise Http404()
    post_to_delete.delete()
    return HttpResponseRedirect('/')

@staff_member_required
def delete_tag(request, tag_id=None):
    data = Tag.objects.get( id=tag_id) 
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













