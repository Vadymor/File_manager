from django.urls import path
from . import views

app_name = 'file_manager'
urlpatterns = [
    path('', views.upload, name='upload'),
    path('result', views.result, name='result')
]
