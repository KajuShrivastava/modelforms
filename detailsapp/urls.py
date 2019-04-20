from django.urls import path
from django.contrib import admin


from detailsapp.views import userDetails

urlpatterns = [
 path('userdetails/',userDetails),
 path('display/', userDetails),
path('', userDetails),

]
