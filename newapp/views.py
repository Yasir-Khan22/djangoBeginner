from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. Views are just functions.
def home(request):
    return render(request, "index.html")
