from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    # Module Group URLs
    path('', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),]