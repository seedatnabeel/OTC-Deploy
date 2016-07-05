from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'meds/index.html'
    response = HttpResponse("<h1>This is the Medications page")
    return render(request, template)

