from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from course.models import Course

class TestGroup(models.Model):
    test_group_id = models.AutoField(primary_key=True)
    test_group_name = models.CharField(max_length=255,unique=True)
    weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])


    def __str__(self):
        return self.test_group_name

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  
    test_group = models.ForeignKey(TestGroup, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.course) + " - " + self.test_name