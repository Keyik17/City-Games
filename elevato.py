import random
import time 
#A list of names has beeen created.
list_of_names = ['Joe', 'Misha', 'Ayan', 'Snow', 'Aidan', 'Khushi', 'Ved', 'Hanz', 'Kapil', 'Elizabeth',]
list_of_jobs = ['Police man', 'Software engineer', 'Data Scientist', 'Teacher', 'Surgeon', 'Musician', 'Journalist', 'Actor', 'Therapist', 'Librarien']
#A class Users has been created with attributes: name, age, current_floor, target_floor.
class Users:
    def __init__(self, name, age, job, current_floor, target_floor):
        self.name = name 
        self.age = age 
        self.job = job
        self.current_floor = current_floor
        self.target_floor = target_floor
        #Check the direction.
        if self.target_floor > self.current_floor:
            self.direction = 'UP'
        else:
            self.direction = 'DOWN'
#A function display_info has been created. 
#The function prints out the information on the waiting list.        
    def display_info(self):
        print('User:', self.name, end='' + ',')
        print(' Age:', self.age, end='' + ',')
        print(' Job:', self.age, end='' + ',')
        print(' Waiting on floor:',self.current_floor, end='' + ',')
        print(' Going to:', self.target_floor)
        
#A function display_arrive_info has been created. 
#The function prints out the information on the arriving list.         
    def display_arrive_info(self):
        print('User:', self.name, end='' + ',')
        print(' Age:', self.age, end='' + ',')
        print(' Job:', self.age, end='' + ',')
        print(' Have arrived to:',self.target_floor, end='' + ',')
        print(' From:', self.current_floor)

#A class elevator has been created. 
#The class consists of attributes: elevator_ID, current_floor, direction
class elevator:
    def __init__(self, elevator_ID, current_floor, direction):
        self.elevator_ID = elevator_ID
        self.current_floor = current_floor
        self.direction = direction
        self.person_in_elevator = []

#A class elevator_manager has been created. 
class elevator_manager:
    def __init__(self, num_people):
        #Assign all my lists to an empty list to append later 
        self.list_of_elevators = []
        self.waiting_list = []
        self.arriving_list = []
        
        #Loop through number of people.
        for i in range(num_people):
            #iterate each name index from the list of people.
            name = list_of_names[i]
            #randomize the age of people
            age = random.randint(8, 60)
            #iterate each job index from the list of jobs.
            job = list_of_names[i]
            #randomize the current floor. 
            current_floor = random.randint(1, 10)
            target_floor = current_floor 
            #if the target floor matches with the current floor go back and loop until it does not match.
            while target_floor == current_floor:
                target_floor = random.randint(1, 10)

            #Generate a user object
            p = Users(name, age, job, current_floor, target_floor)
            self.waiting_list.append(p)
        
#The first floor's id is 001; direction down and the second floor's id is 002, direction is up.
        for a in range(2):
            if a == 0:
                current_floor = 10
                elevator_ID = '001'
            else:
                current_floor = 1
                elevator_ID ='002'
                
            if a == 0:
                direction = 'DOWN'
            else:
                direction = 'UP'
            
            #generate elevator object 
            e = elevator(elevator_ID, current_floor, direction)
            self.list_of_elevators.append(e)
 
#A function print_elevator has been created.
#Displays the information in the elevator including the elevator's ID, current floor, and the elevator's direction.
#Displays the person's information in the elevator including person's name, current floor, and the target floor.
    def print_elevator(self):
        for a in range(2):
            elevator = self.list_of_elevators[a]
            print('___________________', elevator.elevator_ID, elevator.current_floor, elevator.direction,'_____________________')
            for person in elevator.person_in_elevator:
                print(person.name, person.current_floor, '----->', person.target_floor)
            print('____________________________________________________')
            print()
            
    
#A fuction print_waiting has been created.
#Call the display_info function which prints all the information about the user in the waiting list.       
    def print_waiting(self):
        print('_______________________WAIITING LIST_________________________')
        for person in self.waiting_list:
            person.display_info()
        print('____________________________________________________________')
        print()
        
#A fucntion print_arriving has been created.
#Call the display_arrive_info function which prints all the information about the user in the arriving list.         
    def print_arriving(self):
        print('_______________________ARRIVING LIST_________________________')
        for person in self.arriving_list:
            person.display_arrive_info()
        print('____________________________________________________________')
        print()
        
#A function display_manager has been created.
#The function calls out the waiting list, elevator, and arriving functions.     
    def display_manager(self):
        self.print_waiting()
        self.print_elevator()
        self.print_arriving()
 
#A function move_elevator has been created.
#The function moves elevators up and down from my list of two elevators.
#If the elevator goes down, add 1 so that it does not go down to the negative. Do the same if it goes up. 
    def move_elevator(self):
        for elevator in self.list_of_elevators:
            if elevator.direction  == 'DOWN':
                    elevator.current_floor -= 1
            else:
                    elevator.current_floor += 1
            #If if the elevator reached the bottom floor, switch to up.       
            if elevator.current_floor == 1:
                elevator.direction = 'UP'
            #If if the elevator reached the highest floor, switch to down.
            if elevator.current_floor == 10:
                elevator.direction = 'DOWN'
                
#A fucntion move_ppl_in has been created.                   
    def move_ppl_in(self):
#Create an empty list to append later.
        for elevator in self.list_of_elevators:
            empty_list = []
            for person in self.waiting_list:
#If the person's current floor in the waiting list matches with the elevator's floor append the person to my emty list in the elevator. 
                if elevator.current_floor == person.current_floor and elevator.direction == person.direction:
                    elevator.person_in_elevator.append(person)
#Append the person to the emty list and remove it from the waiting list 
                    empty_list.append(person)
            for person in empty_list:
                self.waiting_list.remove(person)
                    
#A fucntion move_ppl_out has been created.                      
    def move_ppl_out(self):
#Create an empty list to append later.
        for elevator in self.list_of_elevators:
            #in this elevator check every person int this elevator wether they want to go out 
            empty_list = []
            for person in elevator.person_in_elevator:
                if person.target_floor == elevator.current_floor:
                    #when person's taget floor matches with the elevator's current floor append it to the arriving list.
                    self.arriving_list.append(person) 
                    #person will be appended to an empty list and removed fromthe waiting
                    empty_list.append(person)
            for person in empty_list:
                elevator.person_in_elevator.remove(person)
#create an object of elevator manager.      
manager = elevator_manager(10)
#Loop until the loop meets the condition and breaks.
while True:
#Add time sleep of 1 second to see what is going on.
#Call the function.
    manager.display_manager()
    time.sleep(2)
    manager.move_ppl_in()
    #call ppl out
    manager.move_ppl_out()
    manager.display_manager()
    time.sleep(1)
    #When poeple arrive to the waiting list break the loop
    if len(manager.arriving_list) == 10:
        print('Yay! You have arrived. Have a great day!')
        break
    print()
    manager.move_elevator()

 
    
    


