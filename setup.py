#!/usr/bin/env python

#AUTHOR: Juan Manuel Rey Escobar

import setuptools

setuptools.setup(name='tfg',
      version= '1.0.0',
      description='Complete planner to solve ASP logic programs',
      url='https://github.com/jmanuelrey/TFG',
      author='Juan Manuel Rey Escobar',
      author_email='jmanuel.rey.escobar@gmail.com',
      license='GPL-3.0',
      packages= setuptools.find_packages(),
      test_suite='TFG.src.tests', 
      zip_safe=False,
      entry_points={
          'console_scripts':[
              'tfg = TFG.__main__:main'
           ]
       }
)
