from django.shortcuts import render
from .models import Proyect
# Create your views here.

def portfolio(request):
    proyects = Proyect.objects.all()
    return render(request,"portfolio/portfolio.html",{'proyects': proyects}) 