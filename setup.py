from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_reuirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[ req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements


setup(
    name='DimondPricePrediction',
    version='0.0.1',
    packages=find_packages(),
    author='Amarnath',
    license='MIT',
    author_email='amarnath1413@gmail.com',
    install_requires=get_reuirements('requirements.txt')
)