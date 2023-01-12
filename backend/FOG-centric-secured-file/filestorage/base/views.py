from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import FileHandler
from django.core.mail import send_mail
from .forms import UserCreationForm
from uuid import uuid4
from django.contrib import messages
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_register(request):
    context = {}
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully')
        return redirect('home')
    context['form'] = form
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('<h1>Wrong username or password</h1>')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def file_upload(request):
    if request.method == 'POST':
        user = request.user
        file = request.FILES['file']
        filename = file.name
        file_instance = FileHandler(user = user, file = file, filename = filename)
        file_instance.save()
        return redirect('home')
    return render(request, 'file_upload.html')

def file_list(request):
    context = {}
    user = request.user
    all_files = FileHandler.objects.filter(user = user)
    if len(all_files) == 0:
        return HttpResponse('<p>No files found for this user.</p>')
    else:
        context['all_files'] = all_files
        return render(request, 'filelist.html', context)

def verify(request, filename):
    context = {}
    if request.user.is_authenticated:
        curr_user = request.user
        secret_code = send_secret_code(curr_user)
        if request.method=='POST':
            key = request.POST['key']
            if key == secret_code:
                return HttpResponse('<p>Verification done</p>')
        return render(request, 'verify.html', context)
    return HttpResponse('<strong>Sorry you are not authorized</strong>')

def delete_file(request, filename):
    FileHandler.objects.delete(filename=filename)
    return redirect('home')

def download_file(request, filename):
    file = FileHandler.objects.get(filename = filename)
    context = {}
    context['file'] = file
    return render(request, 'download.html', context)

def send_secret_code(user):
    curr_user = user
    secret_key = str(uuid4())
    user_email = curr_user.email
    subject = 'Verification Code'
    message = f'The verification code is {secret_key}'
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [user_email])
    return secret_key
