from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('welcome/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
    path('hello/', views.hello, name='hello'),  
    #path('addnew/',views.addnew, name='AddNew'), 
    re_path(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    path('login/', views.login, name='login'), 
]
