from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from algorithm.encryption import encrypt, decrypt
from .models import File_Handler
# Create your views here.
def home(request):
    return render(request, 'home.html')

def userlogin(request):
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

def userregister(request):
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

def userlogout(request):
    logout(request)
    return redirect('/')

def upload_and_encrypt(request):
    context = {}
    if request.method == 'POST':
        filename = request.POST['filename']
        file = request.FILES['file']
        normalfile = file.read()
        with open(f'media/non_enc_file/{filename}', 'wb') as f:
            f.write(normalfile)
        file_path = f'media/non_enc_file/{filename}'
        encrypted_file_path =encrypt(file_path)
        user = request.user
        file_dets = File_Handler(user=user, filename=filename, encrypted_file_path=encrypted_file_path)
        file_dets.save()
        context['enc'] = encrypted_file_path
        return render(request, 'encrypt.html', context)
    return render(request, 'encrypt.html', context)

def list_of_encrypted_file(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        all_file_dets = File_Handler.objects.filter(user = user)
        context['all_files'] = all_file_dets
        return render(request, 'list_files.html', context)
    return HttpResponse('<h1> You are not authenticated cant fetch any list for you, Please go back to previous page.</h1>')

def decrypt_file(request, filename):
    file_dets = File_Handler.objects.get(filename=filename)
    context = {}
    if request.method == 'POST':
        aes_key = request.FILES['aes_key']
        fernet_key = request.FILES['fer_key']
        file_path = file_dets.encrypted_file_path
        filename = file_dets.filename
        decrypt(filename, aes_key, fernet_key)
        
        context['file_path'] = '/' + f'media/temp/{filename}'
        File_Handler.objects.get(filename=filename).delete()

        return render(request, 'decrypt.html', context)
    return render(request, 'decrypt.html', context)
