from django.shortcuts import render

def home(request):
    return render(request,'home.html',)
def login(request):
    return render(request,'home2.html',)
def men(request):
    return render(request,'men.html',)
def women(request):
    return render(request,'women.html',)
def kids(request):
    return render(request,'kids.html',)
# Create your views here.
