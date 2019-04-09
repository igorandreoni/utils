
from setuptools import setup

setup(
   name='utils_git',
   version='0.2',
   description='Module with modeling and data reduction utilities.',
   author='Nadejda Blagorodnova',
   author_email='n.blagorodnova@astro.ru.nl',
   packages=['model', 'photometry', 'utils'],  #same as name
   package_dir={'model': 'src/model', 'photometry':'src/photometry', 'utils':'src/utils'},
   install_requires=['astropy', 'scipy', 'photutils', 'extinction', 'emcee', 'pysynphot', 'corner'], #external packages as dependencies
   
)
