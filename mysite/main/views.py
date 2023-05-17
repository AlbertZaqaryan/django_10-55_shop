from django.shortcuts import render
from .models import Home, Project
# Create your views here.


def index(request):
    home_list = Home.objects.all()[0]
    project_list = Project.objects.all()
    return render(request, 'main/index.html', context={
        'home_list':home_list,
        'project_list':project_list
    })