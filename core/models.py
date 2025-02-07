import secrets

from django.db import models


class Url(models.Model):
    url = models.URLField(max_length=255)
    hashed_url = models.CharField(max_length=10, db_index=True, unique=True)
    pin = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.url} - {self.hashed_url}"

    def save(self, *args, **kwargs):
        if not self.hashed_url:
            self.hashed_url = self.hash_url()
        super().save(*args, **kwargs)

    def hash_url(self):
        token = secrets.token_urlsafe(16)[:10]
        return token

    def get_full_short_url(self, request):
        domain = request.get_host()
        return f"http://{domain}/{self.hashed_url}/"

    def generate_pin(self):
        if not self.pin:
            self.pin = secrets.token_urlsafe(8)[:5]
            self.save()
        return self.pin
