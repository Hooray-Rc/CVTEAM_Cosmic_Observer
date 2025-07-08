from django.shortcuts import render

def home(request):
    return render(request, 'simulation/index.html')
# Create your views here.
'''
def show_system(request):
    return render(request,'simulation/show_system.html')
'''
