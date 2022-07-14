from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'main'),
    path('analyze', views.analyze, name= 'analysis')
]
