from django.db import models
import uuid

class CheckoutSesijaZapis(models.Model):
    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    stripe_kupac_id = models.CharField(max_length=255)
    stripe_checkout_session_id = models.CharField(max_length=255)
    stripe_cijena_id = models.CharField(max_length=255)
    ima_pristup = models.BooleanField(default=False)
    je_zavrseno = models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if self.user:
    #         self.user_uuid = self.user.uuid
    #     super().save(*args, **kwargs)
