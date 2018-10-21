import random
from unittest import TestCase

from pygal_maps_ru.maps import DISTRICTS, District


class TestDistrict(TestCase):
    def test_district(self):
        data = {}
        for key in DISTRICTS.keys():
            data[key] = random.randrange(100000)

        wm = District()
        wm.add('districts', data)
        q = wm.render_pyquery()
        self.assertEqual(len(q('#districts .district')), len(DISTRICTS))
