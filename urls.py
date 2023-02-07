from django.urls import path
from .views import *

urlpatterns=[
    path("wallupload/",wallupload),
    path("amoleddisplay/",amoleddisplay),
    path("darkdisplay/",darkdisplay),
    path("abstractdisplay/",abstractdisplay),
    path("moviesdisplay/",moviesdisplay),
    path("girldisplay/",girldisplay),
    path("naturedisplay/",naturedisplay),
    path("animaldisplay/",animaldisplay),
    path("index/",index1),
    path('userlogin/', userlogin),
    path('userregistration/', userregistration),
    path('indexpage/',main),
    path("adamoleddisplay/",adamoleddisplay),
    path('amoleddelete/<int:id>',amoleddelete),
    path("addarkdisplay/", addarkdisplay),
    path('darkdelete/<int:id>',darkdelete),
    path("adabstractdisplay/", adabstractdisplay),
    path('abstractdelete/<int:id>',abstractdelete),
    path("admoviesdisplay/",admoviesdisplay),
    path('moviesdelete/<int:id>', moviesdelete),
    path("adgirldisplay/",adgirldisplay),
    path('girldelete/<int:id>', girldelete),
    path("adnaturedisplay/", adnaturedisplay),
    path('naturedelete/<int:id>', naturedelete),
    path("adanimaldisplay/", adanimaldisplay),
    path('animaldelete/<int:id>', animaldelete)



]