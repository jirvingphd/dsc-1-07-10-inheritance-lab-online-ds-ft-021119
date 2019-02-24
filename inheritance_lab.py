

Animal=None
Elephant = None
e=None
e2=None


class Animal(object):
    def __init__(self,name=None,weight=None,size=None,species=None,food_type=None,nocturnal=False):        
        self.name = name
        self.size = size #small medium large or enormous
        self.weight = weight
        self.species = species
        self.food_type = food_type #herbivore carivore omnivore
        self.nocturnal = nocturnal
        
    def sleep(self):
        if self.nocturnal == True:
            sleep_at = 'at night'
        else:
            sleep_at = 'during the day'
        return print(f'{self.name} the {self.species} sleeps {sleep_at}.')
            
    def eat(self,food):
        likes_it=[f'{self.name} the {self.species} thinks {self.food_type} is yummy!']
        if self.food_type=='omnivore':
            print(likes_it)
        
        elif food == 'plants' and self.food_type == 'herbivore':
            print(likes_it)
       
        elif food == 'meat' and self.food_type == 'carnivore':
            print(likes_it)
        else:
            print('I dont eat this!')
    

    
    
class Elephant(Animal):
    
    def __init__(self,name=None,weight=None): #,name='Ele',weight=0): #,name,weight):
        super().__init__(name,weight)
        self.species='elephant'
        self.size='enormous'
        self.food_type='herbivore'
        self.nocturnal=False
    
#e=Elephant('Susie',3200)
        
        
#
#print('e2=Elephant(''Joe,weight=32) returns:\n')
#e2=Elephant('Joe',32)
#print(e2.name)
#print(e2.weight)
#print(e2.size)
#
#
#e=Elephant()
#print('e=Elephant() returns:\n')
#print(f'Name is: {e.name}')
#print(e.weight)
#print(e.size)
        
        
class Tiger(Animal):
    
    def __init__(self,name=None,weight=None): #,name='Ele',weight=0): #,name,weight):
        super().__init__(name,weight)
        self.species='tiger'
        self.size='large'
        self.food_type='carnivore'
        self.nocturnal=True
#t=Tiger('Tony',20)        
#print(f'Name is {t.name}, weight is {t.weight}, food_type {t.food_type}')
        
        
class Raccoon(Animal):
    
    def __init__(self,name=None,weight=None): #,name='Ele',weight=0): #,name,weight):
        super().__init__(name,weight)
        self.species='raccoon'
        self.size='small'
        self.food_type='omnivore'
        self.nocturnal=True
        
        
                
class Gorilla(Animal):
    
    def __init__(self,name=None,weight=None): #,name='Ele',weight=0): #,name,weight):
        super().__init__(name,weight)
        self.species='gorilla'
        self.size='large'
        self.food_type='herbivore'
        self.nocturnal=False
        
        
        
        
        
        
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
        
    
    return zoo.append(new_animal)


# Adding requested animals
add_animal_to_zoo(zoo,'elephant','Bob',500)        #
add_animal_to_zoo(zoo,'elephant','Joe',550)        #
add_animal_to_zoo(zoo,'raccoon','John',100)        #
add_animal_to_zoo(zoo,'raccoon','Paul',100)        #
add_animal_to_zoo(zoo,'gorilla','CRAAAZY',400)        
add_animal_to_zoo(zoo,'tiger','Tigger',30)        
add_animal_to_zoo(zoo,'tiger','Tony',75)        
add_animal_to_zoo(zoo,'tiger','Your Mom',180)        




def feed_animals(zoo,time):
    food_list={'omnivore':'plants','carnivore':'meat','herbivore':'plants'}
    for z in zoo:
        
        if (time.lower() == 'day') and (z.nocturnal == False):
            z.eat(food_list[z.food_type])
            
        elif (time.lower() == 'night') and (z.nocturnal==True):
            z.eat(food_list[z.food_type])

feed_animals(zoo,'day')     
feed_animals(zoo,'night')   
