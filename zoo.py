#inheritance-lab_zoo -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:44:14 2019

@author: james
"""

# create an array called zoo


# create add_animal_to_zoo function
# parameters:
    #zoo, array =current state of zoo
    #animal_type
    #name
    #weight
# use animal_type to determine which object to create
# create instance of animal passing name, weight
# append newly created animal to zoo
# return zoo
zoo=[]
#import inheritance_lab
#from inheritance_lab import Animal, Elephant, Tiger,Raccoon,Gorilla
def add_animal_to_zoo(zoo, animal_type, name, weight):
    new_animal_type=animal_type.title()

    # Create a new object, based on animal_type  
    if new_animal_type == 'Elephant':
        new_animal=Elephant(name,weight)
        
    elif new_animal_type == 'Tiger':      
        new_animal=Tiger(name,weight)
        
    elif new_animal_type == 'Raccoon':        
        new_animal=Raccoon(name,weight)
        
    elif new_animal_type=='Gorilla':
        new_animal = Gorilla(name,weight)
    else:
        print('Incorrect animal type')
        
    return new_animal

#new_animal



add_animal_to_zoo(zoo,'gorilla','Joe',322)        #
#print(help(new_animal))
        
    
    
    
    