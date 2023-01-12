from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import account, file_handler, file_handler_three
import uuid
from django.contrib.auth import login, authenticate, logout
from algorithm.encryptor import encrypt, encryptl2
from algorithm.decryptor import decryptl1, decryptl2
from algorithm.encryptor3layer import encrypt3l1, encrypt3l2, encrypt3l3
from algorithm.decryptor3layer import decrypt3l1, decrypt3l2, decrypt3l3
# Create your views here.

def home(request):
    return render(request, 'home.html')

#For Fernet and RSA
def upload_and_encrypt(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            filename = request.POST.get('filename')
            filename = filename + '.bin'
            file = request.FILES["file"]
            user = request.user
            user = account.objects.get(user=user)

            normalFile = file.read()
            with open(f'media/non_enc_file/{filename}', 'wb') as f:
                f.write(normalFile)
            FILE_PATH = 'media/non_enc_file/'+filename
            print(FILE_PATH)
            key1 = encrypt(FILE_PATH)
            key2, encrypted_file_path = encryptl2(FILE_PATH, filename)
            context['key1'] = key1
            context['key2'] = key2
            context['filename'] = filename
            file_dets = file_handler(user=user,filename=filename, fernetkeyl1=key1, fernetkeyl2=key2, encrypted_file_path=encrypted_file_path)
            file_dets.save()
        return render(request, 'encryption_page.html', context)
    return HttpResponse("<h1>You are not authenticated please go back</h1>")

#2FERNER and RSA
def upload_and_encrypt_layer2(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            filename = request.POST.get('filename')
            file = request.FILES["file"]
            user = request.user
            user = account.objects.get(user=user)

            normalfile = file.read()
            with open(f'media/non_enc_file/{filename}', 'wb') as f:
                f.write(normalfile)
            FILE_PATH = 'media/non_enc_file/' + filename

            key1 = encrypt3l1(FILE_PATH)
            key2 = encrypt3l2(FILE_PATH, filename)
            keyl3, encrypted_file_path = encrypt3l3(FILE_PATH, filename)
            
            context['key1'] = key1

            file_dets = file_handler_three(user=user, filename=filename, fernetkeyl1 = key1, fernetkeyl2=key2, fernetkeyl3 = keyl3,encrypted_file_path = encrypted_file_path)
            file_dets.save()
            context['filename'] = filename
        return render(request, 'encryption_page_layer3.html', context)
    return HttpResponse("<h4> Sorry you are not authenticated!!! </h4>")





def list_of_encrypted_file(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        user = account.objects.get(user=user)
        all_file_dets = file_handler.objects.filter(user = user)
        context['all_files'] = all_file_dets
        return render(request, 'list_files.html', context)
    return HttpResponse('<h1> You are not authenticated cant fetch any list for you, Please go back to previous page.</h1>')

def file_list3(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        user = account.objects.get(user=user)
        all_file_dets = file_handler_three.objects.filter(user = user)
        context['all_files'] = all_file_dets
        return render(request, 'list_files3.html', context)
    return HttpResponse('<h1> You are not authenticated cant fetch any list for you, Please go back to previous page.</h1>')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
        return redirect('/')

    return render(request, 'user_login.html')



def user_register(request):
    context = {}
    form = UserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            public_key = uuid.uuid4()
            new_user = account(user=user, public_key=public_key)
            new_user.save()
            login(request, user)
            return redirect('/')
    
    return render(request, 'user_register.html', context)

def show_pub_key(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        find_user = account.objects.get(user=user)
        find_pub_key = find_user.public_key
        context['public_key'] = find_pub_key
        return render(request, 'show_pubkey.html', context)
    return render(request, 'show_pubkey.html', context)

def decrypt_file(request, filename):
    file_dets = file_handler.objects.get(filename=filename)
    context = {}
    if request.method == 'POST':
        key1 = request.FILES['keyl1']
        key2 = request.FILES['keyl2']
        file_path = file_dets.encrypted_file_path
        filename = file_dets.filename
        print(filename)
        decryptl1(file_path, filename)
        decryptl2(filename, key2)
        context['file_path'] = '/' + f'media/non_enc_file/{filename}'

        return render(request, 'decrypt_file.html', context)
    return render(request, 'decrypt_file.html', context)

def decrypt_file2(request, filename):
    file_dets = file_handler_three.objects.get(filename=filename)
    context = {}
    if request.method == 'POST':
        key1 = request.FILES['keyl1']
        key2 = request.FILES['keyl2']
        key3 = request.FILES['keyl3']
        file_path = file_dets.encrypted_file_path
        filename = file_dets.filename
        decrypt3l1(file_path, filename)
        decrypt3l2(filename, key2)
        decrypt3l3(filename, key3)
        context['file_path'] = '/' + f'media/non_enc_file/{filename}'

        return render(request, 'decrypt_file_three.html', context)
    return render(request, 'decrypt_file_three.html', context)
        

def user_logout(request):
    logout(request)
    return redirect('/')