from django.db import models
from user.models import User

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết với User
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name
