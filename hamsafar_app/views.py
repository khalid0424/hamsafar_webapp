from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required , user
from django.contrib import messages
from .models import Hamsafar
from .forms import HamsafarForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hamsafar_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('hamsafar_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

@login_required
def create_hamsafar(request):
    if request.method == 'POST':
        form = HamsafarForm(request.POST)
        if form.is_valid():
            hamsafar = form.save(commit=False)
            hamsafar.user = request.user
            hamsafar.save()
            return redirect('hamsafar_list')
    else:
        form = HamsafarForm()
    return render(request, 'create_hamsafar.html', {'form': form})

@login_required
def hamsafar_list(request):
    hamsafars = Hamsafar.objects.filter(user=request.user)
    return render(request, 'hamsafar_list.html', {'hamsafars': hamsafars})
