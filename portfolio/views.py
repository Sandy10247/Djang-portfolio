from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    # Fetch Project records from DB
    totalRecords = Project.objects.all()
    # Data to the Template
    homeContent = {'projects': totalRecords}
    return render(request, 'portfolio/home.html', context=homeContent)
