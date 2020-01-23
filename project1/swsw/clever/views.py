from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request, 'clever/index.html', {})

