from django.urls import path
from main import views

urlpatterns = [
    path('index',views.index),
    path('dashboard',views.dashboard),
    path('signin',views.signin),
    path('register',views.register),
    path('meeting',views.meeting),
    path('video',views.video),
    path('resources',views.resources),
    path('faq',views.faq),
    path('doctor',views.doctor),

]
