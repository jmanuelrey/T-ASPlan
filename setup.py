#!/usr/bin/env python

#AUTHOR: Juan Manuel Rey Escobar

import setuptools
from TFG.src.main.model.util import mainutils

setuptools.setup(name='ASPlanner',
      version= mainutils.version,
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
              'asplanner = TFG.__main__:main'
           ]
       }
)
