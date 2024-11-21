from django.shortcuts import render
def fun(request,exception):
    return render(request,'404page.html',status=404)
# Create your views here.
