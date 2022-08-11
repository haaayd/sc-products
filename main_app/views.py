from django.shortcuts import render

from django.http import HttpResponse

class Profile: 
    def __init__(self, name, skintype):
        self.name = name
        self.skintype = skintype

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')