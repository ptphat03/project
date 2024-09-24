from django.db import models
from user.models import User
from course.models import Course  # Nhớ import Course từ mô hình của bạn

class PerformanceAnalytic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.DecimalField(max_digits=10, decimal_places=2)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Đảm bảo Course đã được import
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Performance Analytics for {self.user.username}"