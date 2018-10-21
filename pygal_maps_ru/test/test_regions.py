import random
from unittest import TestCase

from pygal_maps_ru.maps import REGIONS, Regions


class TestRegions(TestCase):
    def test_regions(self):
        data = {}
        for key in REGIONS.keys():
            data[key] = random.randrange(100000)

        wm = Regions()
        wm.add('regions', data)
        q = wm.render_pyquery()
        self.assertEqual(len(q('#regions .region')), len(REGIONS))
