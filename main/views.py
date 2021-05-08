from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def dashboard(request):
    return render(request, 'main/dashboard.html',{})

def signin(request):
    return render(request, 'main/signin.html',{})

def register(request):
    return render(request, 'main/register.html',{})

def meeting(request):
    return render(request, 'main/meeting.html',{})

def video(request):
    return render(request, 'main/video.html',{})

def resources(request):
    return render(request, 'main/resources.html',{})

def faq(request):
    return render(request, 'main/faq.html',{})

def doctor(request):
    return render(request, 'main/doctor.html',{})