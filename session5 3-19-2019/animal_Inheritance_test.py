

class Animal:

    def __init__(self,age,lifespan,species,health,diet,sex): #sound):
        #int
        self.age = age
        #int
        self.lifespan = lifespan
        #string
        self.species = species
        #string 1.0 is the healthiest, health decreases as it approaches 0
        #0 is death
        self.health = health
        #list, diet is represented by a list of preferences
        #animal diet  preferences are randomly selected each time you play a game
        #diet is flashed at the beginning of the game and you have to remember it
        self.diet = diet
        #string
        #sex as in male or female
        self.sex = sex
        #sound data
        #self.sound = sound
        # welfare and hunger are both floats
        # they could also be represented by ints equal to 100
        self.welfare = 1.0
        # 1.0 is full 0.5 is hungry, 0.0 is starving
        self.hunger = 1.0

    def makeHappy(self):
        self.welfare += 0.2

#diet goes from healthiest to least heatlhy
#each diet list has 3 items
humanDiet = ["vegetables","bread","twinkies"]
DaveTheFarmer = Animal(48,80,"human",0.7,humanDiet,"male")
#print(DaveTheFarmer.welfare)
#DaveTheFarmer.makeHappy()
#print(DaveTheFarmer.welfare)

class Dog(Animal):
    def __init__(self,age_,lifespan_,species_,health_,diet_,sex_,breed,personality):
        super().__init__(age_,lifespan_,species_,health_,diet_,sex_)
        self.breed = breed
        self.personality = personality

dogDiet = ["ground turkey","kibble","apple pie"]

#having the species variable might be redudant
#there might be a need for a name variable
Fido = Dog(10,15,"dog",0.6,dogDiet,"male","pitbull","friendly")
print(Fido.age)
print(Fido.breed)
print(Fido.diet)
print(Fido.welfare)
Fido.makeHappy()
print(Fido.welfare)
