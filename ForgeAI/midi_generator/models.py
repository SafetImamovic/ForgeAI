from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, default='user', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.message}'