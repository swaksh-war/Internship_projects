from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Doctor, Patient, File_handler, Appointment_dets, Pharmacy, Feedback
from django.http import HttpResponse
from algorithm.encryptor import encrypt, encryptl2, encryptl3
from algorithm.decryptor import decryptl1, decryptl2, decryptl3
from .forms import PharmaForm, FeedBackForm
# Create your views here.

def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('patient_home')
    return render(request, 'patient_login.html')

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('doctor_home')
    return render(request, 'doctor_login.html')

def doctor_home(request):
    context = {}
    if request.user.is_authenticated:
        doc_obj = Doctor.objects.get(user=request.user)
        doc_name = doc_obj.name
        context['name'] = doc_name
        return render(request, 'doctor_home.html', context)
    return HttpResponse('Some error occured! Please Go back')

def patient_home(request):
    context = {}
    if request.user.is_authenticated:
        pat_obj = Patient.objects.get(user = request.user)
        pat_name = pat_obj.name
        context['name'] = pat_name
        return render(request, 'patient_home.html', context)
    return HttpResponse('Some error Occured! Please Go back')

def upload_file(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            filename = request.POST.get('filename')
            file = request.FILES["file"]
            doctor = Doctor.objects.get(user=request.user)
            patient = Patient.objects.get(name=request.POST['patient_name'])
            normalFile = file.read()
            with open(f'media/non_enc_file/{filename}', 'wb') as f:
                f.write(normalFile)
            FILE_PATH = 'media/non_enc_file/'+filename
            key1 = encrypt(FILE_PATH, filename)
            key2, encrypted_file_path = encryptl2(FILE_PATH, filename)
            file_path = encryptl3(filename)
            file_dets = File_handler(doc=doctor, pat=patient ,filename=filename, fernetkey1=key1, fernetkey2=key2, encrypted_file_path=encrypted_file_path)
            file_dets.save()
        return render(request, 'encryption_page.html')
    return HttpResponse("<h1>You are not authenticated please go back</h1>")

def download_file(request, filename):
    file_dets = File_handler.objects.get(filename=filename)
    context = {}
    file_path = file_dets.encrypted_file_path
    filename = file_dets.filename
    decryptl1(filename)
    decryptl2(file_path, filename)
    decryptl3(filename)

    context['file_path'] = '/'+f'media/non_enc_file/{filename}'
    return render(request, 'decrypt_file.html', context)


    

def file_list(request):
    context = {}
    if request.user.is_authenticated:
        user = Patient.objects.get(user = request.user)
        file_list = File_handler.objects.filter(pat=user)
        if len(file_list) != 0:
            context['files'] = file_list
        
            return render(request, 'file_list.html', context)
    return HttpResponse('<h4>No File Found for you you seemed to be fine!</h4>')


def show_appointment(request):
    context={}
    curr_user = request.user
    doctor = Doctor.objects.get(user = curr_user)
    appointments = Appointment_dets.objects.filter(doctor = doctor)
    context['all_appointments'] = appointments
    return render(request, 'view_appointments.html', context)

def pharmacy_add(request):
    form = PharmaForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = PharmaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('doctor_home')
    return render(request, 'pharmacy_add.html', context)

def pharmacy_view(request):
    context = {}
    all_meds = Pharmacy.objects.all()
    context['all_meds'] = all_meds
    return render(request, 'view_pharmacy.html', context)

def add_appointment(request):
    context = {}
    if request.method == 'POST':
        curr_user = request.user
        name = request.POST['name']
        doctor = Doctor.objects.get(user = curr_user)
        time = request.POST['time']
        patient_name = request.POST['patient_name']
        patient = Patient.objects.get(name = patient_name)
        new_appo = Appointment_dets(name = name, doctor=doctor, time = time, patient = patient)
        new_appo.save()
        return redirect('doctor_home')
    return render(request, 'add_appointments.html', context)

def add_feedback(request):
    form = FeedBackForm()
    context= {}
    if request.user.is_authenticated:
        curr_user = request.user
        patient = Patient.objects.get(user = curr_user)
        if patient != None:
            form = FeedBackForm()
            context['feedbackform'] = form
            if request.method == 'POST':
                form = FeedBackForm(request.POST)
                if form.is_valid():
                    form.save()
                return redirect('patient_home')
            return render(request, 'add_feedback.html', context)
        else:
            return HttpResponse("No Patient found with that user instance please contact tech support")
    else:
        return HttpResponse('No user found please contact tech support')

def show_feedback(request):
    context = {}
    if request.user.is_authenticated:
        curr_user = request.user
        doctor = Doctor.objects.get(user = curr_user)
        if doctor != None:
            all_feedbacks = Feedback.objects.filter(doctor = doctor)
        context['all_feedbacks'] = all_feedbacks
        return render(request, 'view_feedback.html', context)
