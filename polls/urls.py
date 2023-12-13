from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    
    path('', views.polls, name='polls'),
    path('<str:poll_name>/', views.poll_detail, name='poll_detail'),
    path('<str:poll_name>/results/', views.poll_results, name='poll_results'), 
]
