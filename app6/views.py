from django.shortcuts import render

# Create your views here.
def jinja1(request):
    d={'name':'mounika'}
    return render(request,'jinja.html',context=d)