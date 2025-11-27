from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hi(request):
   return HttpResponse("Hi there! Welcome to Shadynewapp.")

def runtemplate(request):
      return render(request, 'Shadynewapp/shady.html')