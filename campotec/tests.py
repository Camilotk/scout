# -*- coding:utf-8 -*-

from django.test import TestCase


class CampotecHomePageTest(TestCase):

    def test_details(self):
        response = self.client.get('/campotec/')
        self.assertEqual(response.status_code, 200)
