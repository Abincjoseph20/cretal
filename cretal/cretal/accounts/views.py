from django.shortcuts import render,redirect
from .forms import RegistrationForms
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
# from django.urls import reverse
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)

            user.phone_number=phone_number
            # user.is_active = False
            user.save()

            #user activation
            current_site = get_current_site(request)
            mail_subject = 'please activate your account'
            message = render_to_string('accounts/accounts_verification_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),

            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()

            # to_email = email
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()

            messages.success(request,'Registration successful')
            return redirect('login')
    else:
        form = RegistrationForms()
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out!')
    return redirect('login')

def activate(request):
    return