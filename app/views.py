from django.shortcuts import render

# Create your views here.
def vasu(request):
    d={'name':'mania'}
    return render(request,'vasu.html',d)