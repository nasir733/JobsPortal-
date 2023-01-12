from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
User = get_user_model()


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            if user.email_verified :
                auth.login(request=request, user=user)
                messages.success(request, 'you are logged in ')
                return redirect('/')
            else:
                user.verify_email()
                messages.error(request,'you need to verify your email check your email inbox')
        else:
            messages.error(request, 'invalid credintials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    messages.info(request, "See you later")
    auth.logout(request)
    return redirect("login")


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exits')
                else:
                    user = User.objects.create_user(
                        email=email, password=password)
                    user.save()
                    user.verify_email()
                    messages.success(request, 'Account created succesfully')
                    messages.success(
                        request, 'We Send You An Link To Verify Your Email For Verification ')
                    return redirect('login')

        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    return render(request, 'accounts/register.html')


def complete_verification(request, key):
    try:
        user = User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        messages.success(request,'Your Email Has Been Verified Successfully')
        # to do: add succes message
    except User.DoesNotExist:
        # to do: add error message
        pass
    return redirect('login')


