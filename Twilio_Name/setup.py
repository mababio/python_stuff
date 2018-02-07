from setuptools import setup

setup(name='twilio_name',
      version='1.0',
      description='provide phone number and get name assoicated with it.',
      author='Michael Ababio',
      author_email='michaelkwasi@gmail.com',
      install_requires=['twilio'],
      python_requires=">=3.0",
      entry_points = {'console_scripts': ['twil_num=twilio_name.twilio_helper:main']},
      package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.ini'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
     },
     packages=['twilio_name','config'],
     )
