from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(response):
    if response.method == 'POST':
        form = CustomUserCreationForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('/login')
    else:
        form = CustomUserCreationForm()

    return render(response, 'register/register.html', {'form': form})
