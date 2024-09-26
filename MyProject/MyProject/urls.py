from django.contrib import admin
from django.urls import path , include
from . import views

# handler404 = views.handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ClothApp.urls')),
]
