from pygal_maps_ru.maps import REGIONS, Regions, Regions_en
from pygal.style import LightenStyle
import random

data = {}
dark_lighten_style = LightenStyle('#336676')
for code, name in REGIONS.items():
    data[code] = random.randrange(1000000)


wm = Regions_en(style=dark_lighten_style)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', data)

wm.render_to_file('russia_population.svg')