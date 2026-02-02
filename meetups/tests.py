from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from meetups.models import Meetup, MeetupParticipation

User = get_user_model()


class MeetupModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="organizer", password="password")
        self.meetup_data = {
            "organizer": self.user,
            "title": "Test Meetup",
            "description": "Description",
            "start_datetime": timezone.now() + timedelta(days=1),
            "duration_minutes": 60,
            "location_text": "Remote",
        }

    def test_meetup_creation(self):
        """Test that a valid meetup can be created."""
        meetup = Meetup.objects.create(**self.meetup_data)
        self.assertEqual(
            str(meetup),
            f"[{meetup.pk}] organizer - Test Meetup "
            f"({meetup.start_datetime.strftime('%Y-%m-%d %H:%M')})"
        )

    def test_past_date_validation(self):
        """Test that clean() raises ValidationError for past dates."""
        self.meetup_data["start_datetime"] = timezone.now() - timedelta(days=1)
        meetup = Meetup(**self.meetup_data)
        with self.assertRaises(ValidationError) as cm:
            meetup.full_clean()
        self.assertIn("start_datetime", cm.exception.message_dict)

    def test_end_datetime_property(self):
        """Test the calculated end time property."""
        meetup = Meetup.objects.create(**self.meetup_data)
        expected_end = meetup.start_datetime + timedelta(minutes=60)
        self.assertEqual(meetup.end_datetime, expected_end)


class ParticipationModelTest(TestCase):
    def setUp(self):
        self.org = User.objects.create_user(username="org", password="pass")
        self.guest = User.objects.create_user(
            username="guest", password="pass")
        self.meetup = Meetup.objects.create(
            organizer=self.org,
            title="Open Meetup",
            start_datetime=timezone.now() + timedelta(days=1),
            duration_minutes=60,
            is_open=True
        )

    def test_approve_method(self):
        """Test the transition from PENDING to GOING."""
        participation = MeetupParticipation.objects.create(
            user=self.guest, meetup=self.meetup, status="pending"
        )
        participation.approve()
        self.assertEqual(participation.status, "going")
        self.assertIsNotNone(participation.approved_at)


User = get_user_model()


class MeetupViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="user1", password="password")
        self.user2 = User.objects.create_user(
            username="user2", password="password")
        self.meetup = Meetup.objects.create(
            organizer=self.user1,
            title="User 1 Event",
            start_datetime=timezone.now() + timedelta(days=1),
            duration_minutes=60,
            is_open=False  # Requires approval
        )

    def test_update_permission(self):
        """Test that only the organizer can access the edit page."""
        self.client.login(username="user2", password="password")
        response = self.client.get(
            reverse('meetup_update', kwargs={'pk': self.meetup.pk}))
        # Your handle_no_permission redirects to 'meetup_list'
        self.assertRedirects(response, reverse('meetup_list'))

    def test_toggle_participation_request(self):
        """Test that a guest can request to join a closed meetup."""
        self.client.login(username="user2", password="password")
        url = reverse('toggle_participation', kwargs={'pk': self.meetup.pk})

        # Post to toggle
        response = self.client.post(url)

        # Check if record was created as PENDING because is_open=False
        participation = MeetupParticipation.objects.get(
            user=self.user2, meetup=self.meetup)
        self.assertEqual(participation.status, "pending")
        self.assertRedirects(response, reverse(
            'meetup_detail', kwargs={'pk': self.meetup.pk}))

    def test_organizer_approve_request(self):
        """Test the approve_participation view logic."""
        participation = MeetupParticipation.objects.create(
            user=self.user2, meetup=self.meetup, status="pending"
        )
        self.client.login(username="user1", password="password")  # Organizer
        url = reverse('approve_participation', kwargs={'pk': participation.pk})

        response = self.client.get(url)
        participation.refresh_from_db()

        self.assertEqual(participation.status, "going")
        self.assertRedirects(response, reverse(
            'meetup_detail', kwargs={'pk': self.meetup.pk}))
