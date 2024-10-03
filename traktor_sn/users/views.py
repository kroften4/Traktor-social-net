from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account {username} registered succesfully. You are now able to log in")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Sign up'})
