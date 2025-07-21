from django.db import models
from accounts.models import Profile
class Task(models.Model):
    '''
    Create Task model
    '''
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = "user"