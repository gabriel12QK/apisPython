from django.urls import path
from .views import  studientView


urlpatterns=[
    path('estudiante/', studientView.as_view(), name='studients_list'),
   
]