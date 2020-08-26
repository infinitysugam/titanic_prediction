from django.urls import path
from .import views

urlpatterns=[
     path('',views.home,name='ml-home'),
     path('result/',views.result,name='ml-result')
]