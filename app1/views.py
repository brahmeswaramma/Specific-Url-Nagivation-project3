from django.shortcuts import render

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def virat(request):
    return render(request,'virat.html')