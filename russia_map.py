from pygal_maps_ru.maps import REGIONS, Regions, Regions_en, DISTRICTS, District
from pygal.style import LightenStyle
import random

data = {}
dark_lighten_style = LightenStyle('#336676')
for code, name in DISTRICTS.items():
    data[code] = random.randrange(1000000)


wm = District(style=dark_lighten_style)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', data)

q = wm.render_pyquery()
print(len(q('#districts .district')))
print(len(DISTRICTS))

wm.render_to_file('russia_population_districts.svg')