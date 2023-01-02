from setuptools import setup
from typing import List

#### Declaring variables for setup functions
Project_name = "Houing_precidtor"
Version = "0.0.1"
Author = "sharath chandra "
Description = "This is my first project end to end"
Packages = ['Housing']
Requriments_name = "requirements.txt"

def get_requirements()->list[str]:
    """
    Description : This function is going to return list of 
    requriments mention in reuqriments .txtfile 
    
    return this is function is going to a return a list which contain name of librabries 
    mentain in requriments .txt file 
    """
    with open(Requriments_name) as requriment_file:
        requriment_file.readlines()
        
    
    
setup(
    name=Project_name,
    version= Version,
    author= Author,
    description= Description,
    packages=Packages,
    install__requries = get_requirements()
    
)

if __name__ =="__main__":
    print(get_requirements())
    