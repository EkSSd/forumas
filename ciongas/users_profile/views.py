from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .forms import NewUserForm, EditProfileForm, PasswordEditForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from ciongo_posts.models import Post
from django.contrib.auth.views import PasswordChangeView
from django.template import loader

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


def user_profile( request):
	
    mydata = Post.objects.filter(author_id = request.user.id)
    template = loader.get_template('profile.html')
    context = {
        'object_list': mydata
    }
    return HttpResponse(template.render(context, request))


class EditProfileView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('profile')

	def get_object(self):
		return self.request.user


class PasswordsEditView(PasswordChangeView):
	form_class = PasswordEditForm
	success_url = reverse_lazy('profile')















