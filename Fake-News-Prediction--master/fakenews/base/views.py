from django.shortcuts import render, redirect
# Create your views here.
from . import datapreprocess

def makePrediction(message):
    import joblib
    data = datapreprocess.preprocess(message)
    model = joblib.load('fake_news_new_model.joblib')
    pred = model.predict(data)
    return pred

def home(request):
    if request.method == 'POST':
        message = request.POST['message']

        res = makePrediction(message)
        
        context = {'res':res}
        return redirect('home')
    context = {}
    return render(request,'home.html', context)
    

