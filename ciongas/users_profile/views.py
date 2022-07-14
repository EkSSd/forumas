from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from ciongo_posts.models import Post
from django.contrib.auth.forms import UserChangeForm

# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration success.")
            return HttpResponseRedirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="registration/registration.html", context={"register_form":form})
    

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return HttpResponseRedirect('/')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})




class UserProfileView(LoginRequiredMixin, ListView):
     queryset = Post.objects.all()
     template_name = "profile.html"

def get_queryset(self):
	user = self.request.user
	return Post.objects.filter(author=user)


class EditProfileView(generic.UpdateView):
	form_class = UserChangeForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('profile')

	def get_object(self):
		return self.request.user


















