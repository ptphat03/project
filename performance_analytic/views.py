from django.shortcuts import render
from .models import PerformanceAnalytic

def performance_analytic_list(request):
    performance_analytics = PerformanceAnalytic.objects.all()
    
    # Tính toán progress_percentage
    for analytic in performance_analytics:
        analytic.progress = analytic.progress * 100  # Chuyển đổi thành phần trăm
        # analytic.total_score = analytic.total_score * 100
    return render(request, 'performance_analytic_list.html', {'performance_analytics': performance_analytics})
