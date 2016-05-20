from setuptools import setup

setup(name='flask_react',
      version='0.0.2',
      author='Yang Fan',
      author_email='yangfan@garena.com',
      description='Auto setup tool for flask and react project',
      url='git@github.com:ripitrust/flask_react.git',
      packages=['flask_react'],
      install_requires=['virtualenv'],
      entry_points={'console_scripts': ['flask_react=flask_react.main:main']},
)
