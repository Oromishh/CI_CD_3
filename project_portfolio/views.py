from django.shortcuts import render, get_object_or_404
import datetime

def index(request):
    return render(request, 'index.html')