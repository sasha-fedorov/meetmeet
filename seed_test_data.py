# Creates test users and realistic meetups
# for local testing & after Render free DB resets

# run:
# python manage.py shell
# exec(open('seed_test_data.py', encoding='utf-8').read())

from datetime import timedelta
from django.contrib.auth.models import User
from django.utils import timezone
import random

APP_NAME = "meetups"

try:
    Meetup = __import__(f"{APP_NAME}.models", fromlist=["Meetup"]).Meetup
except (ImportError, AttributeError):
    print("Could not import Meetup model. Check APP_NAME.")
    raise

now = timezone.now()
print(f"Current time: {now}")

# Clean previous test data
User.objects.filter(username__startswith="testuser_").delete()
print("Previous test data deleted")

users = []

names = ["Noah", "Liam", "Olivia", "Amelia", "Mia",
         "Sophia", "Charlotte", "Ava", "Emma", "Luna", "Aria"]

# Populating Users
for i in range(1, 11):
    username = "testuser_" + names[i]
    email = username + "@example.invalid"

    user, created = User.objects.get_or_create(
        username=username,
        defaults={"email": email, "is_staff": False, "is_superuser": False},
    )
    if created or user.password == "":
        user.set_password(username)
        user.save()
        print(f"Created/updated: {username} pass: {username}")

    users.append(user)

organizers = users[1:]

# Meetup titles and descriptions pool
base_events = [
    ("Python coders hangout", "Casual evening — bring your laptop or ideas",
     "Code Cafe on Vorbergstraße"),
    ("Morning trail run 8-12 km",
     "Different pace groups, coffee after", "Berlin Treptower Park"),
    ("Board games & snacks", "We have Catan, Ticket to Ride, Wingspan…",
     "Brettspielplatz - Das Spielecafe"),
    ("Indie film screening + discussion",
     "This time: Everything Everywhere All at Once", ""),
    ("Swing dance beginner lesson", "No partner needed, come alone", ""),
    ("Photo walk - golden hour",
     "Bring camera/phone, city center", ""),
    ("Vegan potluck dinner", "Everyone brings one dish, share recipes",
     "Große Präsidentenstraße 29"),
    ("Startup idea pitch night", "5 min pitch + feedback, no investors yet",
     "https://meet.google.com/"),
    ("Retro console tournament", "Street Fighter, Mario Kart — old CRTs",
     "Berlins erste Arcade Bar & Restaurant"),
    ("Improv comedy workshop",
     "Led by local actor, very beginner friendly", "Comedy Café Berlin"),
    ("Language exchange (EN/DE/FR/ES)",
     "Drinks & conversation tables", "Coffee Connect Berlin"),
    ("DIY electronics meet",
     "Arduino, Raspberry Pi, soldering iron provided", "freeCodeCamp"),
    (
        "Python coders hangout & mini code jam",
        """Casual evening for Python enthusiasts of all levels.\n\n
        We'll start with some lightning intros (30 seconds each), then people
        can either:\n
        - hack on personal projects with others around\n
        - pair on small coding challenges/katas\n
        - just chat about recent changes in 3.11-3.13, typing, FastAPI/HTMX
        trends, etc.\n\n
        Pizza & soft drinks provided (please mention allergies when you RSVP).
        Laptops welcome but not required — many people just come to talk\n\n
        Location has power strips, decent Wi-Fi and a projector in case
        someone wants to show something cool""",
        "freeCodeCamp"
    ),
    (
        "Morning trail run - three pace groups",
        """Weekly Sunday trail run in [Nearby nature park/city outskirts].\n\n
        Three groups this time:\n
        - Beginner/recovery → ~6-7 km, relaxed 6:30-7:30 min/km pace\n
        - Main group → 9-11 km, ~5:30-6:00 min/km\n
        - Fast/progression → 12-14 km, sub-5:20 min/km\n\n
        We meet at 8:00, start running at 8:15.\n
        Coffee & croissant stop afterwards at the little bakery near the
        parking (everyone pays their own).\n\n
        Bring:\n
        - trail or road shoes according to weather\n
        - water bottle/hydration pack\n
        - phone in case we get separated\n\n
        First-timers very welcome — just choose the beginner group""",
        "Berlin Treptower Park"
    ),
    (
        "Board games & snacks - bring one game!",
        """Relaxed board-game evening — no tournament, no stress, just good
        games and conversations.\n\n
        We provide:\n
        - Tables & good lighting\n
        - Catan, Ticket to Ride, Wingspan, 7 Wonders, Cascadia, Splendor\n
        - snacks (chips, nuts, veggies & dip)\n
        - soft drinks, tea, filter coffee\n\n
        Please bring:\n
        - at least one game you love (we'll rotate)\n
        - enthusiasm to teach/learn new games\n\n
        Capacity limited to ~18 people so everyone can actually play
        and not just watch.\n
        We usually do 2-3 rounds, mixing short and medium-length games""",
        "Brettspielplatz - Das Spielecafe"
    ),
    (
        "Indie film screening + open discussion",
        """This month we're watching Everything Everywhere All at Once
        (2022) — if you haven't seen it yet, perfect timing!\n\n
        Plan:\n
        19:00 - doors open, drinks & popcorn\n
        19:30 - start screening (subtitled)\n
        21:10-ish - lights on, informal discussion\n\n
        Topics we usually end up talking about:\n
        - multiverse storytelling & narrative structure\n
        - family dynamics & generational trauma\n
        - absurd humour vs emotional depth\n
        - practical effects & creative fight choreography\n\n
        Feel free to bring your own non-alcoholic drinks/snacks to share.\n
        No spoilers in the chat before the screening please""",
        "b-ware Ladenkino"
    ),
    (
        "Swing dance beginner lesson + social dance",
        """No partner needed, no experience required.\n\n
        19:00-19:45  Beginner lesson (basic 6-count & 8-count patterns)\n
        19:45-22:00  Social dance - mix of beginners &
        more experienced dancers\n\n
        We play mostly classic swing + some neo-swing/electro-swing.\n
        Shoes: clean indoor shoes or dance shoes
        (no street shoes on the parquet).\n\n
        Water cooler on site, small bar with soft drinks & beer (optional).\n
        First lesson is free — after that it's pay-what-feels-fair (~€5-8)""",
        "Dance Cafe"
    ),
    (
        "Golden hour photo walk - urban edition",
        """Meet at [famous viewpoint/bridge/square] at 16:45.\n\n
        We walk for ~90 minutes chasing nice light, reflections, leading lines,
        street details, portraits — whatever inspires you.\n\n
        All camera types welcome: phone, compact, mirrorless, film…\n
        We usually stop 2-3 times to look at each other's shots and give quick
        friendly feedback.\n\n
        Ends around 18:30 near [nice café/pub] — optional coffee/beer
        afterwards (self-paid)""",
        "Starting at S+U Potsdamer Platz"
    ),
    (
        "Vegan potluck dinner & recipe swap",
        """Everyone brings one vegan dish (savoury or sweet) to share.\n\n
        Ideas that always work well:\n
        - hummus + veggies + flatbread\n
        - lentil dal/chickpea curry\n
        - pasta salad with pesto & grilled veggies\n
        - brownies/energy balls/fruit salad\n
        - homemade falafel or spring rolls\n\n
        We provide:\n
        - plates, cutlery, big tables\n
        - still & sparkling water, tea\n
        - music playlist\n\n
        Please write ingredients/allergens on a small note next to your dish.\n
        Bring your own container if you want to take leftovers home""", ""
    ),
    (
        "Startup idea pitch night - no investors, just feedback",
        """Format: 4-6 pitches, 4 minutes presentation + 6 minutes feedback /
        questions.\n\n
        You can present:\n
        - very early idea (pre-MVP)\n
        - working prototype/landing page\n
        - side project looking for direction\n
        - re-positioning an existing product\n\n
        No slides required — whiteboard, phone screen, description, all fine.\n
        Goal is honest, constructive feedback from other founders /
        tech people / potential users.\n\n
        Drinks & snacks provided""", ""
    ),
]


created_count = 0

# Populating Meetups
for _ in range(35):
    organizer = random.choice(organizers)

    title_base, desc, location = random.choice(base_events)

    variation = random.choice([
        ".", " vol.2.", " spring '26.", " #3.", " reloaded.",
        " - bigger edition.", " meetup.", " gathering.", " session.",
    ])

    if random.random() < 0.70:
        variation = "."
    else:
        # 30% chance to pick one of the "fancy" titles
        variation = random.choice(
            [" vol.2.", " #3.", " reloaded.", " meetup."])

    title = f"{title_base}{variation}"

    days_offset = random.triangular(-60, 90, mode=10)
    hours_offset = random.randint(-12, 36)

    start = now + timedelta(days=days_offset, hours=hours_offset)

    is_open = random.random() < 0.7

    max_part = None
    if random.random() < 0.6:
        max_part = random.choice([6, 8, 10, 12, 15, 18, 22, 30, 40, 60])

    duration_minutes = random.choice(
        [60, 80, 120, 150, 180, 220, 300, 400, 600, 1000])

    Meetup.objects.create(
        organizer=organizer,
        title=title,
        description=desc,
        location_text=location,
        duration_minutes=duration_minutes,
        max_participants=max_part,
        is_open=is_open,
        start_datetime=start,
        # created_at / updated_at = auto
    )
    created_count += 1


print(f"\nCreated {len(users)} users + {created_count} meetups.")
