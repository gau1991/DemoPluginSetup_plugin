import os
from setuptools import setup

abspathconfig = '/root/.myapp/plugins.d'
abspathplugins = '/root/.myapp/plugins'

if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)



setup(name='Demo Plugin',
      version='0.1',
      description='Demo Plugin',
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      data_files=[(abspathconfig, ['testplugin/plugn.conf']),
                  (abspathplugins, ['testplugin/plugn.py'])],
      # packages=['cli'],
      install_requires=[
          'abc',
      ],
      
      zip_safe=False)