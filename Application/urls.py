from django.urls import path
from . import views

urlpatterns = [ 
        path('',views.login, name = ' login'),
        path('dashboard/', views.dashboard , name = 'dashboard'),
        path('award/',views.award, name = 'award'),
        

        path('bank/',views.bank, name = 'bank'),
        path('bitcoin/',views.bitcoin, name = 'bitcoin'),

]