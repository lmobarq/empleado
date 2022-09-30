from django.contrib import admin
from django.urls import path

from . import views 


urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view()),
    #arriba se pone lista con - en medio y no como en view.py en home con _ bajo
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(), 
        name='resume_foundation'
    ),
]