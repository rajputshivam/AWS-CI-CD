from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    reqirements = []
    with open(file_path) as file_obj:
        reqirements = file_obj.readlines()
        reqirements = [req.replace("\n","") for req in reqirements]

        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)

    return reqirements


setup(
    name='mlproject',
    version='0.0.1',
    author ='Shivam',
    author_email='rajputshivam.cse@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)