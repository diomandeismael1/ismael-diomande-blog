from django.shortcuts import render
from .models import Publication

# Create your views here.
def index(request):
    list_publication=Publication.objects.all
    context={'list_publication':list_publication}
    return render(request,'blog/index.html',context)


#def detail(request,id):
