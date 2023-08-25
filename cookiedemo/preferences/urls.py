from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_language, name='set_language'),
    path('get/', views.get_language, name='get_language'),
]