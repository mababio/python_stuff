"""
Author: Michael Ababio
Date: 02-06-2017
Purpose: configuring app setup
"""

from setuptools import setup, find_packages
#ANYTHING ENCLOSED IN [] NEEDS TO BE REPLACED.

setup(name='[appname]',
      version='0.0.1',
      description='',
      author='Michael Ababio',
      author_email='michaelkwasi@gmail.com',
      install_requires=['boto3'],
      python_requires=">=3.0",
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      zip_safe=False,
      entry_points={'console_scripts': ['[cmd_line]=[app dirname].[app.py]:main']},
      package_data={
          # Making sure that the config.ini is packaged:
          '': ['*.ini'],
          # And include any *.msg files found in the 'hello' package, too:
          'hello': ['*.msg']
      }
     )
