from django.urls import path
from . import views

app_name = 'performance_analytic'

urlpatterns = [
    path('', views.performance_analytic_list, name='performance_analytic_list')]