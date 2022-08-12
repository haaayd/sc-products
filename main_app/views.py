from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define the home view
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def profiles_index(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/index.html', { 'profiles': profiles })

@login_required
def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    return render(request, 'profiles/detail.html', { 'profile': profile })

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['name', 'comment', 'skin_type', 'time']
    success_url = '/profiles/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['name', 'comment', 'skin_type', 'time']

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model= Profile
    success_url = '/profiles/'

def signup(request):
    error_message = ""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profiles_index')
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)