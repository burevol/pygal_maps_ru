# pygal_maps_ru  

Russian maps for Pygal

[![PyPI](https://img.shields.io/pypi/v/pygal-maps-ru.svg)](https://pypi.org/project/pygal-maps-ru/)
[![GitHub last commit](https://img.shields.io/github/last-commit/burevol/pygal_maps_ru.svg)](https://github.com/burevol/pygal_maps_ru)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pygal-maps-ru.svg)](https://pypi.org/project/pygal-maps-ru/)

## Installation

~~~
pip install  pygal-maps-ru 
~~~

## Usage

~~~~
import pygal.maps.ru

map = pygal.maps.ru.Regions()
map.add('Data', {'KHM': 2, 'KYA': 5})
map.render_to_file('test.svg')

~~~~

More instruction on [https://github.com/burevol/pygal_maps_ru/wiki](https://github.com/burevol/pygal_maps_ru/wiki)

## Requirements

* [Pygal](https://github.com/Kozea/pygal) 

## Author
[burevol](https://github.com/burevol)   
SVG map by [SmartTeleMax](https://github.com/SmartTeleMax)
