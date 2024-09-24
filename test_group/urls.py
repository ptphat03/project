from django.urls import path
from . import views

app_name='test_group'

urlpatterns = [
    path('', views.test_group_list, name='test_group_list'),
    path('<int:pk>/', views.test_group_detail, name='test_group_detail'),
    path('add/', views.test_group_add, name='test_group_add'),
    path('<int:pk>/edit', views.test_group_edit, name='test_group_edit'),
    path('<int:pk>/delete', views.test_group_delete, name='test_group_delete'),


    path('test/', views.test_list, name='test_list'),
    path('test/<int:pk>/', views.test_detail, name='test_detail'),
    path('test/add/', views.test_add, name='test_add'),
    path('test/<int:pk>/edit', views.test_edit, name='test_edit'),
    path('test/<int:pk>/delete', views.test_delete, name='test_delete'),

]