#Author: Ogulkeyik Annagulyyeva
#Advised by Jianghao Wang
import names
import random
#Create a list of colors, weather, and counties.
color_list = ['Sweet Sugarplum.', 'Toasted Almond.', 'Dusk Blue.', 'Lucite Green.', 'Titanium.', 'Crysatalline.', 'White Heron.', 'Golden Straw.', 'Hint of Lavender.']
weather = ['heavy rain!', 'thunder storm!', 'rainbow!', 'clear sky!']
country = ['Scotland.', 'Germany.', 'Japan.', 'Finland.', 'Sweden.', 'Austria.']

# Create a class named house which consists of values: address, people, color, rooms, pets, and the number of flowers in the garden.
class house:
#Initialize all my neccessary values/ attributes.
    def __init__(self, address, color, people,  rooms, pets, flowers_in_the_garden):
        self.address = str(address)
        self.people = [people]
        self.color = color
        self.rooms = rooms
        self.pets = pets
        self.flowers_in_the_garden = flowers_in_the_garden

#Create a function that makes people.
#This function iterates a list of people and prints people from that list.
    def print_people(self):
        print('People: ', end ='')
        for p in self.people:
            print(p, end ='')
        print()
#Create a function that displays the information provided.
#Call my print_people function in get_info. 
    def get_info(self):
        print('******************************')
        print()
        print('Address: ', self.address)
        self.print_people()
        print('Roof color: ', self.color)
        print('Rooms: ', self.rooms)
        print('Pets: ', self.pets)
        print('Flowers in the garden: ', self.flowers_in_the_garden)
        print()
#Create a class called cul-de-sac.
class cul_de_sac:
    def __init__(self, num_houses):
#Craete an empty list of houses to pass the values later on.
        self.list_of_houses = []
#Randomly generate an index and access the wetaher condition from the list.
        index_w = random.randint(0,3) 
        self.weather = weather[index_w]
#Randomly generate an index and access the country from the list.
        index = random.randint(0,5)
        self.country = country[index]
#Randomize the number of attributes.
        for i in range(num_houses):
            address = 1000 + i
            rooms = random.randint(2, 10)
            pets = random.randint(0, 4)
            flowers_in_the_garden = random.randint(500, 2567)
            color = random.choice(color_list)
#Append all the information in the house class to my list of houses which I created in __init__ function.
            self.list_of_houses.append(
                house(address, color, names.get_first_name(), rooms, pets, flowers_in_the_garden)
            ) 
# Display the information regarding teh weather and the country to my cul-de-sac.
    def get_info(self):
        weather_a = random.randint(0,4)
        print('We are in the ', self.country)
        print('Expect', self.weather)
        for house in self.list_of_houses:
            house.get_info()
#Move people from one house to another.
#This function takes an index from my list of houses and holds it in a temporary variable ( create a copy of the person);
#remove the person from the house and append it to another house.
    def move(self, address_1, address_2):
        for a in range(len(self.list_of_houses)):
            if address_1 == self.list_of_houses[a].address:
                print('Found address 1!')
                temp = self.list_of_houses[a].people
                self.list_of_houses[a].people = []
        for b in range(len(self.list_of_houses)):
            if address_2 == self.list_of_houses[b].address:
                self.list_of_houses[b].people.extend(temp)

#Generate a random number of houses.
n = random.randint(4,6)
#Use my class to create a cul-de-sac object.
final = cul_de_sac(n) 

#Create a main loop so that the program iterates forever.
while True:
    final.get_info()
#Allow the user to enter the addres
    choose = input('To move people, please enter two address numbers: ')
    a_1, a_2= choose.split()
    print(a_1, a_2)
#Call the function and pass the values to values.
    final.move(a_1, a_2)
