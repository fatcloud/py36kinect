try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pykinect',
      version='0.1',
      description='kinect v1 driver',
      author='Cloud',
      author_email='cloud@seabunny.tech',
      packages=['pykinect', 'pykinect.nui'],
      install_requires=[
          'numpy',
          'matplotlib',
          'pygame',
          'future',
      ],
      zip_safe=False)
