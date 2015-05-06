import os
from setuptools import setup

abspathconfig = '/etc/ee/plugins.d'

if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)


setup(name='Demo Plugin 4 ee',
      version='0.2',
      description='Demo Plugin',
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      data_files=[(abspathconfig, ['testplugin/plugn4ee.conf'])],
      # packages=['cli'],
      install_requires=[
          'ee',
      ],

      zip_safe=False)
