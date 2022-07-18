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
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
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


# class UserProfileView(LoginRequiredMixin, ListView):
#      queryset = Post.objects.all()
#      template_name = "profile.html"


# def get_queryset(self):
# 	user = self.request.user
# 	return Post.objects.filter(author=user)



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


# def password_reset_request(request):
# 	if request.method == 'POST':
# 		password_form = PasswordResetForm(request.POST)
# 		data = password_form.cleaned_data.get('email')
# 		user_email = User.objects.filter(Q(email=data))
# 		if user_email.exists():
# 			for user in user_email:
# 				subject = 'Password Requests'
# 				email_template_name = 'password_message.txt'
# 				parameters = {
# 					'email': user.email,
# 					'domain': 'localhost:8000',
# 					'site_name': 'ChibridSite',
# 					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 				}
# 				email = render_to_string(email_template_name, parameters)
# 				try:
# 					send_mail(subject, email, '', [user.email], fail_silently=False,)
# 				except:
# 					return HttpResponse('Invalid header')
# 				return redirect('password_reset_done')
# 	else:
# 		password_form = PasswordResetForm()
# 	context = {
# 		'password_form': password_form,

# 	}
# 	return render(request, 'registration/password_reset.html', context)













