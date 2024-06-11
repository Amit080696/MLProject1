from setuptools import find_packages, setup



setup(
name ='mlproject',
version='0.0.1',
author='Amit Baghel',
author_email='amit.bharat999@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
