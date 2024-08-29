from django.shortcuts import render, redirect
from .models import Shop, Item_type
from .forms import CreationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse


# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    articles = Shop.objects.filter(item_type__product_name__icontains=q)

    item_types = Item_type.objects.all()

    context = {'articles':articles, 'item_types':item_types}
    return render(request, 'base/home.html', context)



def details(request, pk):
    article = Shop.objects.get(pk=pk)
    context = {'article':article}
    return render(request, 'base/details.html', context)


#@login_required(login_url='login')
def add(request):
    form = CreationForm()
    if request.method == "POST":
        form= CreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/form.html', context)



@login_required(login_url='login')
def delete(request, pk):
    article = Shop.objects.get(pk=pk)
    article.delete()
    return redirect('home')



@login_required(login_url='login')
def update(request, pk):
    article = Shop.objects.get(pk=pk)
    form = CreationForm(instance=article)
    if request.method == "POST":
        form = CreationForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('details', pk)
    context = {'form':form, 'article':article}
    return render(request, 'base/form.html', context)


def signup(request):
    form= UserCreationForm()
    if request.method== 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    context= {'form': form}
    return render(request, 'base/signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        # return HttpResponse(user)
        
        if user is not None:
            login(request, user)
            
            return redirect('home')
        return HttpResponse('form not valid')
    return render(request, 'base/login.html')


def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return render(request, 'base/logout.html')



