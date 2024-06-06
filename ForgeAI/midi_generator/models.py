from django.db import models
from django.contrib.auth.models import User
import uuid

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=255, default='user', blank=True, null=True)
    type = models.CharField(max_length=255, default='user', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    midi_link = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.message}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return self.id