class Pet:
    all_pets = []
    def __init__(self, name):
        self.name = name
        Pet.all_pets.append(self)

    @classmethod
    def first_pet(cls):
        if cls.all_pets:
            return cls.all_pets[0]
        return None
    
    @classmethod
    def last_pet(cls):
        if cls.all_pets:
            return cls.all_pets[-1]
        return None
    
    @classmethod
    def num_of_pets(cls):
        return len(cls.all_pets)
    
print(Pet.first_pet()) 
print(Pet.last_pet()) 
print(Pet.num_of_pets()) 

pet1 = Pet('Ratchet') 
pet2 = Pet('Clank') 
pet3 = Pet('Rivet') 
print(Pet.first_pet().name) 
print(Pet.last_pet().name) 
print(Pet.num_of_pets()) 