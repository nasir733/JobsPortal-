from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from users.forms import LoginForm, RegisterForm

# Create your views here.
User = get_user_model()


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
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
                messages.error(
                    request, 'Incorrect Details')
                
        else:
       
            messages.error(
                request, f'invalid credintials ')
            return render(request, 'accounts/login.html', {'form': form})
    else: 
        form = LoginForm()
    return render(request, 'accounts/login.html',{'form':form})


def logout(request):
    messages.info(request, "See you later")
    auth.logout(request)
    return redirect("login")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return render(request, 'accounts/register.html', {'form': form})
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exits')
                    return render(request, 'accounts/register.html', {'form': form})
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
            return render(request, 'accounts/register.html',{'form':form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html',{'form':form})


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


