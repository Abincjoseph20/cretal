# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.password_validation import validate_password
# from django.contrib import auth
# from . import views



from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .models import User
# from .forms import RegistrationForms
# from django.views.decorators.cache import cache_control
#
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def Register(request):
#
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = RegistrationForms(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             mobile = form.cleaned_data['mobile']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             username = email.split("@")[0]
#             user = User.objects.create_user(first_name=first_name,
#                                             last_name=last_name,
#                                             email=email,
#                                             username=username,
#                                             mobile=mobile,
#                                             password=password
#                                             )
#
#             messages.success(request, 'signup successfull, activation link is sent to the registerd email ')
#             return redirect('home') #return redirect('login')
#     else:
#         form = RegistrationForms()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/register.html', context)
# user.save()
# current_site = get_current_site(request)
# mail_subject = 'please activate your account'
# message = render_to_string('user_temp/user_email_verfication.html', {
#     'user': user,
#     'domain': current_site,
#     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#     'token': default_token_generator.make_token(user),
# })
# to_email = email
#
# send_email = EmailMessage(mail_subject, message, to=[to_email])
# send_email.send()




from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegistrationForm

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
