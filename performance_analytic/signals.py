from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from student_performance.models import StudentPerformance
from .models import PerformanceAnalytic
from user.models import User
from django.db.models import Sum, F, DecimalField

@receiver(post_save, sender=StudentPerformance)
def update_performance_analytics(sender, instance, created, **kwargs):
    # Cập nhật bảng PerformanceAnalytics khi có bản ghi mới
    update_performance(instance.user_id)

@receiver(post_delete, sender=StudentPerformance)
def delete_performance_analytics(sender, instance, **kwargs):
    # Xóa dữ liệu trong PerformanceAnalytics nếu bản ghi đã bị xóa
    PerformanceAnalytic.objects.filter(user_id=instance.user_id).delete()
    update_performance(instance.user_id)
    
def update_performance(user_id):
    # Tính tổng score và progress
    result = (
        StudentPerformance.objects
        .filter(user_id=user_id)
        .values('user_id', 'test_id__course_id')  # Thêm course_id vào values
        .annotate(
            total_score=Sum(F('score') * F('test_id__test_group__weight'), output_field=DecimalField()),
            progress=Sum('test_id__test_group__weight'),
        )
    )

    # Cập nhật hoặc tạo mới PerformanceAnalytics
    for res in result:
        user_instance = User.objects.get(user_id=res['user_id'])  # Lấy instance của User
        
        PerformanceAnalytic.objects.update_or_create(
            user=user_instance,  # Cung cấp instance của User
            course_id=res['test_id__course_id'],  # Sử dụng course_id từ kết quả
            defaults={
                'total_score': res['total_score'],
                'progress': res['progress'],
            }
        )