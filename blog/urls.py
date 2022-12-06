from .import views
from django.urls import path

urlpatterns = [
    path("kripto/",views.kripto, name="kripto"),
    path("yazilim/",views.yazilim, name="yazilim"),
    path("matematik/",views.matematik, name="matematik"),
     path("iletisim/",views.iletisim, name="iletisim"),
   
    path("iletisim/",views.iletisim, name="iletisim"),
    path("kripto_detay/<slug:slug>",views.kripto_detay, name="kripto_detay"),
    path("yazilim_detay/<slug:slug>",views.yazilim_detay, name="yazilim_detay"),
     path("matematik_detay/<slug:slug>",views.matematik_detay, name="matematik_detay")
    
    
    
    
]
