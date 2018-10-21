from pygal_maps_ru.maps import REGIONS, REGIONS_EN, Regions, Regions_en, DISTRICTS, District, DISTRICTS_EN, District_en
from pygal.style import LightenStyle
import random

data_region = {}
data_region_en = {}
data_district = {}
data_district_en = {}

style1= LightenStyle('#336676')
style2= LightenStyle('#886622')
style3= LightenStyle('#116699')
style4= LightenStyle('#551144')

for code, name in REGIONS.items():
    data_region[code] = random.randrange(1000000)

for code, name in REGIONS_EN.items():
    data_region_en[code] = random.randrange(1000000)

for code, name in DISTRICTS.items():
    data_district[code] = random.randrange(1000000)

for code, name in DISTRICTS_EN.items():
    data_district_en[code] = random.randrange(1000000)

wm_region = Regions(style=style1)
wm_region_en = Regions_en(style1=style2)
wm_district = District(style=style3)
wm_district_en = District_en(style=style4)

wm_region.add("regions",data_region)
wm_region_en.add("regions_en", data_region_en)
wm_district.add("districts", data_district)
wm_district_en.add("districts_en", data_district_en)

wm_region.render_to_file('test_russia_map_regions.svg')
wm_region_en.render_to_file('test_russia_map_regions_en.svg')
wm_district.render_to_file('test_russia_map_districts.svg')
wm_district_en.render_to_file('test_russia_map_districts_en.svg')
