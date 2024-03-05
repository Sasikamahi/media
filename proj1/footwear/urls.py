from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('kids',views.kids,name='kids'),
]

