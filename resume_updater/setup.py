#from setuptools import setup
from setuptools import setup, find_packages

setup(name='resume_updater',
      version='0.0.2',
      description='Uploads file to aws S3 service.',
      author='Michael Ababio',
      author_email='michaelkwasi@gmail.com',
      install_requires=['boto3'],
      python_requires=">=3.0",
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      zip_safe=False,
      entry_points = {'console_scripts': ['resume_updater=resume_updater.S3Copy:main']},
      package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.ini'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
      #packages=['resume_updater'],
     )
