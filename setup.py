import os, json
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

v = json.loads(read("VERSION"))
__version__ = "%i.%i.%i" % (v['version_major'],v['version_minor'],v['version_patch'])

setup(
    name='smstools',
    version=__version__,
    description='Universal SMS conversion tool',
    long_description=read('README.rst'),
    author='Tim O\'Brien',
    author_email='timo@t413.com',
    packages=['smstools', 'smstools.tests'],
    scripts=['bin/smstools'],
    url='https://github.com/t413/SMS-Tools',
    license='CC BY-NC-SA 3.0 US',
    install_requires=['python-dateutil', 'setuptools'],
    extras_require = {
        'colors':  ["blessings>=1.5.0"],
        'autocomplete':  ["argcomplete>=0.8.0"],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
