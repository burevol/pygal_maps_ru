# -*- coding: utf-8 -*-

# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.
"""
Russia chart
"""

# TODO Add english localization

# TODO Add tests

from __future__ import division
from pygal.graph.map import BaseMap
import os

REGIONS = {
    'IRK': 'Иркутская область',
    'TOM': 'Томская область',
    'KHM': 'Ханты-Мансийский АО — Югра',
    'PER': 'Пермский край',
    'TVE': 'Тверская область',
    'SMO': 'Смоленская область',
    'VOR': 'Воронежская область',
    'VGG': 'Волгоградская область',
    'SAR': 'Саратовская область',
    'ORE': 'Оренбургская область',
    'KYA': 'Красноярский край',
    'SA': 'Саха (Якутия)',
    'MAG': 'Магаданская область',
    'KAM': 'Камчатский край',
    'PRI': 'Приморский край',
    'ZAB': 'Забайкальский край',
    'BEL': 'Белгородская область',
    'KLU': 'Калужская область',
    'MOS': 'Московская область',
    'VLA': 'Владимирская область',
    'NIZ': 'Нижегородская область',
    'CU': 'Чувашия',
    'ME': 'Марий Эл',
    'TA': 'Татарстан',
    'SAM': 'Самарская область',
    'ROS': 'Ростовская область',
    'KDA': 'Краснодарский край',
    'KC': '	Карачаево-Черкесия',
    'KB': 'Кабардино-Балкария',
    'STA': 'Ставропольский край',
    'DA': 'Дагестан',
    'ALT': 'Алтайский край',
    'NVS': 'Новосибирская область',
    'KEM': 'Кемеровская область',
    'KK': 'Хакасия',
    'BU': 'Бурятия',
    'AMU': 'Амурская область',
    'SAK': 'Сахалинская область',
    'TY': 'Тыва',
    'YEV': 'Еврейская АО',
    'CHU': 'Чукотский АО',
    'YAN': 'Ямало-Ненецкий АО',
    'ARK': 'Архангельская область',
    'PSK': 'Псковская область',
    'KOS': 'Костромская область',
    'VLG': 'Вологодская область',
    'LEN': 'Ленинградская область',
    'MUR': 'Мурманская область',
    'TAM': 'Тамбовская область',
    'PNZ': 'Пензенская область',
    'KIR': 'Кировская область',
    'KO': 'Коми',
    'SEV': 'Севастополь',
    'CR': 'Крым',
    'AD': 'Адыгея',
    'BA': 'Башкортостан',
    'AL': 'Алтай',
    'IN': 'Ингушетия',
    'KL': 'Калмыкия',
    'KR': 'Карелия',
    'MO': 'Мордовия',
    'SE': 'Северная Осетия — Алания',
    'UD': 'Удмуртия',
    'CE': 'Чечня',
    'KHA': 'Хабаровский край',
    'AST': 'Астраханская область',
    'BRY': 'Брянская область',
    'IVA': 'Ивановская область',
    'KGD': 'Калининградская область',
    'KGN': 'Курганская область',
    'KRS': 'Курская область',
    'LIP': 'Липецкая область',
    'NGR': 'Новгородская область',
    'OMS': 'Омская область',
    'ORL': 'Орловская область',
    'RYA': 'Рязанская область',
    'SVE': 'Свердловская область',
    'TUL': 'Тульская область',
    'TYU': 'Тюменская область',
    'ULY': 'Ульяновская область',
    'CHE': 'Челябинская область',
    'YAR': 'Ярославская область',
    'NEN': 'Ненецкий АО',
    'SPE': 'Санкт-Петербург',
    'MOW': 'Москва',
}

REGIONS_EN = {
    'IRK': 'Irkutsk Region',
    'TOM': 'Tomsk Region',
    'KHM': 'Khanty-Mansi Autonomous Area – Yugra',
    'PER': 'Perm Territory',
    'TVE': 'Tver Region',
    'SMO': 'Smolensk Region',
    'VOR': 'Voronezh Region',
    'VGG': 'Volgograd Region',
    'SAR': 'Saratov Region',
    'ORE': 'Orenburg Region',
    'KYA': 'Krasnoyarsk Territory',
    'SA': 'Republic of Sakha (Yakutia)',
    'MAG': 'Magadan Region',
    'KAM': 'Kamchatka Territory',
    'PRI': 'Primorye Territory',
    'ZAB': 'Trans-Baikal Territory',
    'BEL': 'Belgorod Region',
    'KLU': 'Kaluga Region',
    'MOS': 'Moscow Region',
    'VLA': 'Vladimir Region',
    'NIZ': 'Nizhny Novgorod Region',
    'CU': 'Chuvash Republic',
    'ME': 'Republic of Mari El',
    'TA': 'Republic of Tatarstan',
    'SAM': 'Samara Region',
    'ROS': 'Rostov Region',
    'KDA': 'Krasnodar Territory',
    'KC': '	Karachayevo-Circassian Republic',
    'KB': 'Kabardino-Balkarian Republic',
    'STA': 'Stavropol Territory',
    'DA': 'Republic of Daghestan',
    'ALT': 'Altai Territory',
    'NVS': 'Novosibirsk Region',
    'KEM': 'Kemerovo Region',
    'KK': 'Republic of Khakassia',
    'BU': 'Republic of Buryatia',
    'AMU': 'Amur Region',
    'SAK': 'Sakhalin Region',
    'TY': 'Republic of Tuva',
    'YEV': 'Jewish Autonomous Region',
    'CHU': 'Chukotka Autonomous Area',
    'YAN': 'Yamal-Nenets Autonomous Area',
    'ARK': 'Arkhangelsk Region',
    'PSK': 'Pskov Region',
    'KOS': 'Kostroma Region',
    'VLG': 'Vologda Region',
    'LEN': 'Leningrad Region',
    'MUR': 'Murmansk Regionь',
    'TAM': 'Tambov Region',
    'PNZ': 'Penza Region',
    'KIR': 'Kirov Region',
    'KO': 'Komi Republic',
    'SEV': 'Sevastopol',
    'CR': 'Republic of Crimea',
    'AD': 'Republic of Adygeya',
    'BA': 'Republic of Bashkortostan',
    'AL': 'Republic of Altai',
    'IN': 'Republic of Ingushetia',
    'KL': 'Republic of Kalmykia',
    'KR': 'Republic of Karelia',
    'MO': 'Republic of Mordovia',
    'SE': 'Republic of North Ossetia – Alania',
    'UD': 'Udmurtian Republic',
    'CE': 'Chechen Republic',
    'KHA': 'Khabarovsk Territory',
    'AST': 'Astrakhan Region',
    'BRY': 'Bryansk Region',
    'IVA': 'Ivanovo Region',
    'KGD': 'Kaliningrad Region',
    'KGN': 'Kurgan Region',
    'KRS': 'Kursk Region',
    'LIP': 'Lipetsk Region',
    'NGR': 'Novgorod Region',
    'OMS': 'Omsk Region',
    'ORL': 'Orel Region',
    'RYA': 'Ryazan Region',
    'SVE': 'Sverdlovsk Region',
    'TUL': 'Tula Region',
    'TYU': 'Tyumen Region',
    'ULY': 'Ulyanovsk Region',
    'CHE': 'Chelyabinsk Region',
    'YAR': 'Yaroslavl Region',
    'NEN': 'Nenets Autonomous Area',
    'SPE': 'St. Petersburg',
    'MOW': 'Moscow',
}

with open(os.path.join(
        os.path.dirname(__file__),
        'russia.svg')) as file:
    RUSSIA_MAP = file.read()


class Regions(BaseMap):
    """Russia graph"""
    x_labels = list(REGIONS.keys())
    area_names = REGIONS
    area_prefix = 'RU-'
    svg_map = RUSSIA_MAP
    kind = 'region'

class Regions_en(BaseMap):
    """Russia graph english"""
    x_labels = list(REGIONS_EN.keys())
    area_names = REGIONS_EN
    area_prefix = 'RU-'
    svg_map = RUSSIA_MAP
    kind = 'region'

