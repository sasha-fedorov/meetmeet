from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Meetup(models.Model):
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_meetups"
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    max_participants = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Leave empty for unlimited participants."
    )

    start_datetime = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    location_text = models.CharField(
        max_length=255,
        help_text="Physical location or short description."
    )

    online_link = models.URLField(
        null=True,
        blank=True,
        help_text="Optional link for online meetups."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Default sorting field"""
        ordering = ["start_datetime"]

    def __str__(self):
        return f"{self.title} "\
            "({self.start_datetime.strftime('%Y-%m-%d %H:%M')})"

    def clean(self):
        """Custom validation rules."""
        if self.start_datetime < timezone.now():
            raise ValidationError("Meetup cannot be scheduled in the past.")

        if self.online_link and not self.online_link.startswith(
                ("http://", "https://")):
            raise ValidationError("Online link must be a valid URL.")

    @property
    def end_datetime(self):
        """Calculate meetup end time."""
        return self.start_datetime + timezone.timedelta(
            minutes=self.duration_minutes
        )
