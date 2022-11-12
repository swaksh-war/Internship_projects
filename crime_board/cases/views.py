from django.shortcuts import render, redirect, HttpResponse
from .models import Crimecase
from .forms import crimeaddform
# Create your views here.
def case_index(request):
    all_case = Crimecase.objects.all()
    context = {'all_case':all_case}
    return render(request,"cases_home.html", context)

def add_crime(request):
    if request.method == 'POST':
        case_name = request.POST.get('case_name')
        case_desc = request.POST.get('case_desc')
        case_date = request.POST.get('case_date')
        case_cover = request.POST.get('cover_photo')
        case_loc = request.POST.get('case_loc')
        case_cat = request.POST.get('case_category')
        instance = Crimecase(case_cover=case_cover, case_name=case_name, case_desc=case_desc, case_date=case_date, case_loc = case_loc, case_category = case_cat)
        instance.save()
        return redirect('home')
    return render(request, 'crime_add.html')

def add_crime_form(request):
    caseform = crimeaddform()
    if request.method == 'POST':
        caseform = crimeaddform(request.POST)
        if caseform.is_valid():
            caseform.save()
            return redirect('home')
    return render(request, 'crime_add_form.html', {'form':caseform})
