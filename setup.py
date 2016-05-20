from setuptools import setup

setup(name='flask_react',
      version='0.0.1',
      author='Yang Fan',
      author_email='yangfan@garena.com',
      description='Auto setup tool for flask and react project',
      #url='https://gitsa.garenanow.com/yangfan/Ultron-agent',
      packages=['flask_react'],
      install_requires=['virtualenv'],
      entry_points={'console_scripts': ['flask_react=project.main:main']},
)
