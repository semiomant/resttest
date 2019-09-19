from django.shortcuts import render

def jqfront(request):
    return render(request,'hello.html',{})
