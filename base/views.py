from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .scraper import scrape_links_from_website
from .forms import RegistrationForm
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def page(request):
    return render(request, "homepage/index.html")
def contactus(request):
    return render(request, "contactus/contactus.html")

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)
        
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/mainpage")
        else:
            return render(request, 'login/login.html')
    return render(request, "login/login.html")

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/mainpage")  # Redirect to main page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'login/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the homepage or any other page after logout



def mainpage(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    return render(request, "mainpage/main.html")

def scrape_links(request):
    if request.user.is_anonymous:
        return redirect("/signin")
    url = 'https://www.techgig.com/webinar/tag/data%20science'
    links = scrape_links_from_website(url)
    return render(request, 'search_page/links.html', {'links': links})

class TaskList(ListView):
    model=Task
    template_name="task_list.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("/signin")
        return super().dispatch(request, *args, **kwargs)
    
class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
    template_name='task_create.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("/signin")
        return super().dispatch(request, *args, **kwargs)