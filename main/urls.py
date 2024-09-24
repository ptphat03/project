from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  

app_name = 'main'

urlpatterns = [
    # Your other URL patterns
    path('', views.home, name='home'),

]
