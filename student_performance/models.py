from django.db import models
from user.models import User
from test_group.models import Test

class StudentPerformance(models.Model):
    performance_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    test = models.ForeignKey(Test, on_delete=models.CASCADE)  
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(null=True, blank=True)
 
    def __str__(self):
        return str(self.performance_id)

    
