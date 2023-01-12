from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Account, FileHandler
import requests
import uuid
from django.http import HttpResponse
from algorithm import encryptor, decryptor
import os
# Create your views here.

def home(request):
    return render(request, 'home.html')


def user_register(request):
    context = {}
    form = UserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = user.username
            public_key = uuid.uuid4()
            new_user =Account(user = user, public_key = public_key)
            new_user.save()
            #Now lets save into the 3rd party server
            trd_prty = requests.post('http://localhost:8001/api/basic/', data = {'user':name, 'auth_token': public_key})
            res = trd_prty.json()
            if res['status'] == 'user added':
                return redirect('home')
            elif res['status'] == 'error':
                return HttpResponse('<h1>There was an error on third party server</h1>')
    return render(request, 'user_register.html', context)

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('auther')
    return render(request, 'user_login.html', context)

def two_factor_authenticate(request):
    if request.method == 'POST':
        auth_token = request.POST['auth_token']
        username = request.user.username
        trd_prt = requests.get(f'http://localhost:8001/api/basic/{username}/{auth_token}')
        res = trd_prt.json()
        if res['status'] == 'verified':
            return redirect('home')
        elif res['status'] == 'not verified':
            return HttpResponse('<h1>Wrong auth token</h1>')
        elif res['status'] == 'User not found':
            return HttpResponse('<h1>User not found in the 3rd party server</h1>')
    return render(request, 'tfa.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def view_public_key(request):
    context = {}
    instance = Account.objects.get(user = request.user)
    pub_key = instance.public_key
    context['pub_key'] = pub_key
    return render(request, 'view_public_key.html', context)


def upload_and_encrypt(request):
    context = {}
    if request.method == 'POST':
        filename = request.POST['filename']
        file = request.FILES['file']
        normalfile = file.read()
        with open(f'media/non_enc_files/{filename}', 'wb') as f:
            f.write(normalfile)
        file_path = f'media/non_enc_files/{filename}'
        encrypted_file_path =encryptor.encryption(file_path)
        user = request.user
        account_instance = Account.objects.get(user=user)
        file_dets = FileHandler(user=account_instance, filename=filename, encrypted_file_path=encrypted_file_path)
        file_dets.save()
        context['enc'] = encrypted_file_path
        return render(request, 'encrypt.html', context)
    return render(request, 'encrypt.html', context)

def list_of_encrypted_file(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        account_instance = Account.objects.get(user = user)
        all_file_dets = FileHandler.objects.filter(user = account_instance)
        context['all_files'] = all_file_dets
        return render(request, 'list_files.html', context)
    return HttpResponse('<h1> You are not authenticated cant fetch any list for you, Please go back to previous page.</h1>')

def decrypt_file(request, filename):
    file_dets = FileHandler.objects.get(filename=filename)
    context = {}
    if request.method == 'POST':
        fernet_key = request.FILES['fer_key']
        file_path = file_dets.encrypted_file_path
        filename = file_dets.filename
        decryptor.decryption(filename, fernet_key)
        
        context['file_path'] = '/' + f'media/temp/{filename}'
        FileHandler.objects.get(filename=filename).delete()

        return render(request, 'decrypt.html', context)
    return render(request, 'decrypt.html', context)