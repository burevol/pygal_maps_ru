import random
from unittest import TestCase

from pygal_maps_ru.maps import REGIONS_EN, Regions_en


class TestRegions_en(TestCase):
    def test_regions(self):
        data = {}
        for key in REGIONS_EN.keys():
            data[key] = random.randrange(100000)

        wm = Regions_en()
        wm.add('regions', data)
        q = wm.render_pyquery()
        self.assertEqual(len(q('#regions .region')), len(REGIONS_EN))
