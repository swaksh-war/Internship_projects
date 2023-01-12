from django.shortcuts import render, redirect
from .models import File_handler
from algorithm import AES_algo as aes
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, 'home.html')


def upload_and_encrypt(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            file = request.FILES['file']
            filename = file.name
            user = request.user

            normalfile = file.read()
            with open(f'media/non_enc_file/{filename}', 'wb') as f:
                f.write(normalfile)
            FILE_PATH = 'media/non_enc_file/' + filename
            # Now encryption Phase Comes in
            path = aes.generate_key(filename)
            encrypted_file_path = aes.encaes(FILE_PATH, filename)
            file_dets = File_handler(
                user=user, filename=filename, enctrypted_file_path=encrypted_file_path)
            file_dets.save()
            context['key_img'] = path
        return render(request, 'encrypt.html', context)
    return HttpResponse('<h1>You are not authenticated</h1>')


def decrypt_and_download(request, filename):
    context = {}
    if request.method == 'POST':
        img = request.FILES['key_image']
        image_data = img.read()
        with open(f'media/key_upload/{filename}_aeskey.png', 'wb') as f:
            f.write(image_data)
        file_path = '/' + f'media/non_enc_file/{filename}'
        context['file_path'] = file_path
        return render(request, 'decrypt.html', context)
    return render(request, 'decrypt.html', context)


def file_list(request):
    if request.user.is_authenticated:
        context = {}
        user = request.user
        all_file_dets = File_handler.objects.filter(user=user)
        if len(all_file_dets) == 0:
            return HttpResponse('<h2>No file Can be fetched! Looks like you havent encrypted any file</h2>')
        context['all_files'] = all_file_dets
        return render(request, 'file_list.html', context)
    return HttpResponse('<h2>Looks like there are some errors!</h2>')

def UserRegister(request):
    context = {}
    form = UserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, 'user_register.html', context)

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        elif user is None:
            return HttpResponse('<h2>User not Found Error!!</h2>')
    return render(request, 'user_login.html')

def UserLogout(request):
    logout(request)
    return redirect('home')