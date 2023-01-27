#import base
import os
import string    
import random # define the random module  

def rand_string():
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string with letters + numeric data.  
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S))  
    return ran

def create_dir():
    # random Directory name
    directory = rand_string()
    
    # Parent Directory path
    parent_dir ='G:\Toy_etl_project\masters_data'
    
    # Path
    path = os.path.join(parent_dir, directory)
    
    # Create the directory
    os.mkdir(path) 
    print(path)
    return path 



 
