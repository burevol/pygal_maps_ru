import random
from unittest import TestCase

from pygal_maps_ru.maps import DISTRICTS_EN, District_en


class TestDistrict_en(TestCase):
    def test_district(self):
        data = {}
        for key in DISTRICTS_EN.keys():
            data[key] = random.randrange(100000)

        wm = District_en()
        wm.add('districts', data)
        q = wm.render_pyquery()
        self.assertEqual(len(q('#districts .district')), len(DISTRICTS_EN))
