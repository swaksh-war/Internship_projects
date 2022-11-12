from django.shortcuts import render, redirect, HttpResponse
from .forms import criminaladdform
from .models import Criminal
from cases.models import Crimecase
# Create your views here.
def criminal_index(request):
    all_criminals = Criminal.objects.all()
    context = {'all_criminals':all_criminals}
    return render(request,"criminal_home.html", context)

# def add_criminal(request):
    all_cases = Crimecase.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        pnum = request.POST.get('pnum')
        image = request.POST.get('image')
        case = request.POST.get('case')
        instance = Criminal(name=name, location=location, pnum=pnum, image=image, cases=case)
        instance.save()
        return redirect('home')
    return render(request, 'criminal_add.html', {'all_cases':all_cases})

def add_criminal(request):
    form = criminaladdform()
    if request.method == 'POST':
        form = criminaladdform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'criminal_add.html', {'form':form})