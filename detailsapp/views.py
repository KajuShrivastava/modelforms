from django.shortcuts import render
from django.db import models
from detailsapp.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory

# Create your views here.

from .forms import UserModelForm


def userDetails(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            users = UserDetails.objects.all()

            return render(request, 'display.html', {'users': users})



    else:
        form_class = UserModelForm

    return render(request, 'index.html', {
        'form': form_class,
    })