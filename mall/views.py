from django.shortcuts import render,get_object_or_404
from .models import Mall

# Create your views here.

def home(req):
    malls = Mall.objects.all()
    return render(req, 'home.html', {'malls': malls})

def detail(req, mall_id):
    mall = get_object_or_404(Mall, pk=mall_id)
    return render(req, 'detail.html', {'mall':mall})