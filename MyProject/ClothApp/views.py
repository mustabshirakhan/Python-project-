from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import loader
from ClothApp.models import Welcome
from ClothApp.forms import LoginForm
#def handler404(request, exception):
#   return render(request,'404handler.html')

def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'login.html', {"username" : username})

def hello(request):
    return redirect("https://github.com/")

def welcome(request):
    users=Welcome.objects.all().values()
    template =loader.get_template('hello.html')
    context= {
        'users' : users,     
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    user = Welcome.objects.get(id= id)
    template = loader.get_template('details.html')
    context = {
        'user': user,
     }
    return HttpResponse(template.render(context,request))

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
      'name': 'Kiran',  
  }
  return HttpResponse(template.render(context, request))