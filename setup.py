from setuptools import setup

setup(name='pywm-fullscreen',
      version='0.3',
      description='pywm reference implementation',
      url="https://github.com/jbuchermn/pywm",
      author='Jonas Bucher',
      author_email='j.bucher.mn@gmail.com',
      packages=['pywm_fullscreen'],
      scripts=['bin/pywm-fullscreen', 'bin/.pywm-fullscreen'],
      install_requires=[])
