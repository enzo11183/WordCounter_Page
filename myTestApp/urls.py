from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'), 
    path('sonuc',views.sonuc, name='sonuc'),
    
    path('detay',views.detay, name='detay')
]    