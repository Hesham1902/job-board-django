from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request,user)
            else:
                raise PermissionError('Invalid signing up, Try again later!')
            return redirect('/accounts/profile')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html', {"form": form})
