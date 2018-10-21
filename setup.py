from setuptools import setup, find_packages

setup(
    name='pygal_maps_ru',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/burevol/pygal_maps_ru',
    license='GNU LGPL v3+',
    author='Burevol',
    author_email='alexum2013@yandex.ru',
    description='Russian maps for Pygal',
    platforms="Any",
    provides=['pygal_maps_ru'],
    keywords=[
        "svg", "chart", "graph", "maps", "russian"],
    package_data={'pygal_maps_ru': ['*.svg']},
    install_requires=["pygal>=1.9.9"],
    entry_points={
        'pygal.maps': [
            'ru = pygal_maps_ru.maps',
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: Presentation"]
)

