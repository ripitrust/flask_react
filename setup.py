from setuptools import setup

setup(name='flask_react',
      version='0.0.5',
      author='chrimmme',
      author_email='ripitrust@gmail.com',
      description='Auto setup tool for flask and react project',
      url='https://github.com/ripitrust/flask_react.git',
      download_url='https://github.com/ripitrust/flask_react/tarball/0.0.5',
      packages=['flask_react'],
      install_requires=['virtualenv'],
      entry_points={'console_scripts': ['flask_react=flask_react.main:main']},
)
