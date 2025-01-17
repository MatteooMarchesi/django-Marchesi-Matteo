from django.urls import path 
from .views import home, articoloDetailViewCB, ArticoloListView, GiornalistaListView, GiornalistaDetailViewCB

app_name='news'

urlpatterns=[
    path('',home,name="homeview"),
    path("articoli/<int:pk>",articoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/",ArticoloListView.as_view(),name="lista_articoli"),
    path("giornalista/<int:pk>",GiornalistaDetailViewCB.as_view(), name="giornalista_detail"),
    path("lista_giornalisti/",GiornalistaListView.as_view(),name="lista_giornalisti"),
    
]