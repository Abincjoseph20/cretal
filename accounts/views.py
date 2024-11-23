from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponse


from django.shortcuts import render, redirect
from .forms import RegistrationForms  # Adjust import based on your project structure
from .models import Account  # Your user model
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site


from django.shortcuts import render, redirect
from .models import Account  # Import your Account model



from carts.views import _cart_id
from carts.models import Cart_items,Carts


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

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.phone_number = phone_number
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'please activate your account'
            message = render_to_string('accounts/accounts_verification_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            # User activation email logic goes here...
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form = RegistrationForms()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Carts.objects.get(cart_id=_cart_id(request))  # Get the cart of the session
                cart_items = Cart_items.objects.filter(cart=cart, is_active=True)
                if cart_items.exists():  # Ensure there are active cart items
                    for item in cart_items:
                        item.user = user  # Assign the logged-in user to the cart item
                        item.save()  # Save the updated cart item
            except Carts.DoesNotExist:
                pass  # If no cart exists for the session, do nothing

            auth.login(request, user)  # Log the user in
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



def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'congratulations! your accoun is activated')
        return redirect('login')
    else:
        messages.error(request,'invalid actiavaton link')
        return redirect('login')
        

 # Import your token generator
