from django.urls import path
from . import views
app_name = 'student_performance'

urlpatterns = [
    path('', views.student_performance_list, name='student_performance_list'),
    path('<int:pk>/', views.student_performance_detail, name='student_performance_detail'),
    path('create/', views.student_performance_add, name='student_performance_add'),
    path('<int:pk>/edit/', views.student_performance_edit, name='student_performance_edit'),
    path('<int:pk>/delete/', views.student_performance_delete, name='student_performance_delete'),
]
