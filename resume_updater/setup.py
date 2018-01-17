from setuptools import setup

setup(name='resume_updater',
      version='0.1',
      description='Uploads file to aws S3 service.',
      author='Michael Ababio',
      author_email='michaelkwasi@gmail.com',
      install_requires=['boto3'],
      python_requires=">=3.0",
      entry_points = {'console_scripts': ['resume_updater=resume_updater.S3Copy:main']},
      packages=['resume_updater'],
     )
