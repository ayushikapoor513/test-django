from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name="index"),
    path('final',views.final,name="add")
]