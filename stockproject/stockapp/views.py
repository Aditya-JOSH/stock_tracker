from django.shortcuts import render

def stockpicker(request):
    return render(request,"stockapp/stocktracker.html")