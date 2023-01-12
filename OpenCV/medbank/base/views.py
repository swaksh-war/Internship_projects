from django.shortcuts import render, redirect
from .models import Medicine, Ngo, Donor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import re
from django.db.models import Q

def ExtractDetails(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang = 'eng')
    print(text)
    text = text.replace('\n', " ")
    text = text.replace('  '," ")
    regex_expdate = re.compile('EXP.\d{2}[-/]\d{4}')

    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.axis('off')

    if len(regex_expdate.findall(text)) == 0:
        print(f'Blurry Image for tesseract please upload a new one')
    else:
        text = regex_expdate.findall(text)
        print(text)


def home(request):
    return render(request, 'home.html')

def register_donor(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = User(username=user, password=password)
        user.save()
        donor = Donor(user=user)
        donor.save()
        return redirect('home')
    return render(request, 'registerDonor.html')

def register_ngo(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        gov_reg = request.POST['gov_reg']
        contact = request.POST['contact']
        email = request.POST['email']
        user = User(username=username, password=password)
        user.save()
        ngo = Ngo(user=user, name=name, gov_recognition=gov_reg, contact=contact, email=email)
        ngo.save()
        return redirect('home')
    return render(request, 'registerNgo.html')

def login_donor(request):
    if request.method == 'POST':
        usrname = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usrname, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'loginDonor.html')

def login_ngo(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'loginNgo.html')

def custom_logout(request):
    logout(request)
    return redirect('home')

def upload_med(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['med_name']
        quantity = request.POST['med_quantity']
        expiry_date = request.POST['med_expiry_date']
        category = request.POST['category']
        image = request.FILES['med_image']
        med = Medicine(user=user ,name=name, quantity=quantity, exp_date=expiry_date, category=category, image = image)
        med.save()
        filepath = f'media/{med.image}'
        try:
            ExtractDetails(filepath)
        except:
            pass
        return redirect('home')
    return render(request, 'upload_med.html')

def view_med(request):
    context = {}
    all_med = Medicine.objects.all()
    pass_list = []
    for med in all_med:
        exp_time = med.exp_date.timestamp()
        print(exp_time)
        today = datetime.datetime.today().timestamp()
        if today < exp_time:
            pass_list.append(med)
    
    context['all_meds'] = pass_list
    return render(request, 'view_med.html', context)

def about_us(request):
    return render(request, 'aboutus.html')

def search_query(request):
    context = {}
    if request.method == 'GET':
        query = request.GET['q']
        if query == '':
            query = None
        all_med = Medicine.objects.filter(Q(category__icontains = query) | Q(name__icontains = query))
    context['all_meds'] = all_med
    return render(request, 'search_res.html', context)

