from django.shortcuts import render,redirect
from item.models import Item, Category
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)[:4]
    categories = Category.objects.all()[:4]
    return render(request, 'core/index.html', {'items':items, 'categories':categories})


def contacts(request):
    return render(request, 'core/contacts.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            form = SignupForm()
        return render(request, 'core/signup.html', {'form': form})
    else:
        return redirect('/dashboard/')


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                uname = request.POST.get('username').strip()
                upass = request.POST.get('password')
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    return redirect('/dashboard/')

        else:
            form = LoginForm()
        return render(request, 'core/login.html', {'form': form})
    else:
        return redirect('/dashboard/')

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')



def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'core/dashboard.html', {'user': request.user})
    else:
        return redirect('/login/')
    
            