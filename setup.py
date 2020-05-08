
from setuptools import setup, find_packages

setup(name='mlLogger',
      version='0.1',
      description='A local data science project manager.',
      long_description='A local data science project manager.',
      keywords='A local data science project manager.',
      author='Shubhamkumar Pandey',
      author_email='b18194@students.iitmandi.ac.in',
      license='MIT', # or any license you think is relevant
      packages=find_packages(),
      zip_safe=False,
      install_requires=[ 
          'click',
          'virtualenv',
          'setuptools',
          'mysql-connector-python',
      ],
      entry_points={
        'console_scripts': [
            'mlLogger = mlLogger:base',
        ],
      }
)