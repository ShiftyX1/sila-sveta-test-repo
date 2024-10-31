from django.db import models
import random
import string

class URL(models.Model):
    original_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choices(characters, k=6))
            if not URL.objects.filter(short_url=short_url).exists():
                return short_url
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)
