from django.db import models

class Mix(models.Model):
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='mixes/')

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or "Gallery Image"


class Booking(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate Event'),
        ('birthday', 'Birthday Party'),
        ('club', 'Club/Nightclub'),
        ('festival', 'Festival'),
        ('private', 'Private Party'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='private')
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_date}"


class Notification(models.Model):
    TYPES = [
        ('booking', 'Booking'),
        ('comment', 'Comment'),
    ]

    notification_type = models.CharField(max_length=20, choices=TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.notification_type}: {self.title}"