from django.shortcuts import render

def jqfront(request):
    return render(request,'hello_jq.html',{})

def formfront(request):
    return render(request,'hello_form.html',{})
