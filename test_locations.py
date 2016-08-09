from unittest import TestCase

from location import Locations


class TestLocations(TestCase):
    locations = None

    def setUp(self):
        self.locations = Locations(client_id='b3e2bf83b14747e89cb526adf934563c',
                                   client_secret='7855bdc2ae4341468784204895aaa0a6',
                                   client_ips='189464193',
                                   access_token='189464193.b3e2bf8.1a1a1f0696a84017b1c4bac1443f892e',
                                   redirect_uri=None)
        self.location_id = "1"

    def test_locations_info(self):
        response = self.locations.locations_info(self.location_id)
        self.assertEqual(response.status_code, 200)

    def test_locations_rcent_media(self):
        response = self.locations.locations_recent_media(self.location_id)
        self.assertEqual(response.status_code, 200)

    def test_locations_search(self):
        response = self.locations.locations_search(facebook_places_id=1)
        self.assertEqual(response.status_code, 200)
