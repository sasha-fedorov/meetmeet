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

    is_open = models.BooleanField(
        default=True,
        help_text="If false, users must request approval to join."
    )

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


class MeetupParticipation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending approval"
        GOING = "going", "Going"
        MAYBE = "maybe", "Maybe"
        NOT_GOING = "not_going", "Not going"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="meetup_participations"
    )

    meetup = models.ForeignKey(
        "Meetup",
        on_delete=models.CASCADE,
        related_name="participations"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "meetup")
        ordering = ["-requested_at"]

    def __str__(self):
        return f"{self.meetup}: {self.user} ({self.status})"

    def approve(self):
        """Approve a pending participation request."""
        self.status = self.Status.GOING
        self.approved_at = timezone.now()
        self.save(update_fields=["status", "approved_at"])

    def reject(self):
        """Reject a participation request."""
        self.status = self.Status.NOT_GOING
        self.save(update_fields=["status"])

    @property
    def is_approved(self):
        return self.status != self.Status.PENDING
