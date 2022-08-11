from django.shortcuts import render
from .models import Profile


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/index.html', { 'profiles': profiles })

def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/detail.html', { 'profile': profile })