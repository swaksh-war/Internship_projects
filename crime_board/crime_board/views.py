from django.shortcuts import render, redirect
from cases.models import Crimecase
from criminal.models import Criminal
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from models.get_val_from_model import  get_graph_from_model, get_criminal_analysis


def index(request):

    return render(request,"home.html")

def search_result(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query == '':
            query = None
        cases_list = Crimecase.objects.filter(Q(case_category__icontains = query) | Q(case_loc__icontains= query)) 
        criminal_list =  Criminal.objects.filter(Q(name__icontains=query) | Q(pnum__icontains = query))
        if len(cases_list) > 0:
            context = {'cases_list':cases_list}
        else:
            context = {'criminal_list' : criminal_list}
        return render(request, 'render_result.html',  context=context)

def login_user(request):
    if request.method == 'POST':

        usrname = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usrname, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def predict_crime(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('q')
        if query== '':
            query = None

        _cases = Crimecase.objects.filter(Q(case_loc__icontains=query))
        case_type = []
        for case in _cases:
            case_type.append(case.case_category)
        res = get_graph_from_model(case_type)
        pie_image = r'/media/plotted_graph/pie.png'
        hist_image = r'/media/plotted_graph/hist.png'
        context['pie_image'] = pie_image
        context['res'] = res
        context['hist_image'] = hist_image
        print("Image generated check folder")
        return render(request, 'case_analysis_page.html', context)
    return render(request, 'case_analysis_page.html')

def predict_criminal(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('q')
        if query == '':
            query = None
        
        _cases = Crimecase.objects.filter(Q(case_category__icontains=query))
        criminal_list = []
        for case in _cases:
            criminal_list.append(case.case_criminal)
        res = get_criminal_analysis(criminal_list)
        context['res'] = res
        context['criminal_pie'] = r'/media/plotted_graph/crim_pie.png'
        context['criminal_bar'] = r'/media/plotted_graph/criminal_hist.png'
        
        return render(request, 'criminal_analysis_page.html', context)
    return render(request, 'criminal_analysis_page.html', context)