from unittest import TestCase

from app_info import AppInfo
from insta_py import InstagramAPI


class TestLocations(TestCase):
    locations = None

    def setUp(self):
        instagramAPI = InstagramAPI(access_token=AppInfo.access_token)
        self.locations = instagramAPI.locations
        self.location_id = "1"

    def test_locations_info(self):
        response = self.locations.locations_info(self.location_id)
        self.assertEqual(response.status_code, 200)

    def test_locations_rcent_media(self):
        response = self.locations.locations_recent_media(self.location_id)
        self.assertEqual(response.status_code, 200)

    def test_locations_search(self):
        response = self.locations.search(facebook_places_id=1)
        self.assertEqual(response.status_code, 200)
