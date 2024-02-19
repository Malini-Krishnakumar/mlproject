from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'
def get_requirments(file_path:str)->list[str]:
    '''
    this fuction will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for  req in requirments ]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
    return requirments
    



setup(
name = 'mlproject',
version='0.0.1',
author='Malini',
author_email = 'malukanch@gmail.com',
packages = find_packages(),
install_requires = get_requirments('requirments.txt')

)