import unittest
from unittest.mock import patch


class Event:
    def __init__(self, name, date, location, tickets_available, price, social_media_links):
        self.name = name
        self.date = date
        self.location = location
        self.tickets_available = tickets_available
        self.price = price
        self.social_media_links = social_media_links

    def post_on_social_media(self):
        print(
            f"Join us for {self.name} on {self.date} at {self.location}! Tickets available at {self.social_media_links}. #ArtsInIndia #EmergingTalent")


class TestEvent(unittest.TestCase):

    def test_event_creation(self):
        event = Event("Dance Performance", "June 10, 2023", "Bangalore",
                      75, 750, "https://www.example.com/dance-performance")
        self.assertEqual(event.name, "Dance Performance")
        self.assertEqual(event.date, "June 10, 2023")
        self.assertEqual(event.location, "Bangalore")
        self.assertEqual(event.tickets_available, 75)
        self.assertEqual(event.price, 750)
        self.assertEqual(event.social_media_links,
                         "https://www.example.com/dance-performance")

    def test_post_on_social_media(self):
        event = Event("Regional Theatre Performance", "April 20, 2023",
                      "Mumbai", 100, 500, "https://www.example.com/regional-theatre")
        expected_output = "Join us for Regional Theatre Performance on April 20, 2023 at Mumbai! Tickets available at https://www.example.com/regional-theatre. #ArtsInIndia #EmergingTalent"


unittest.main()
