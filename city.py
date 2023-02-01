#Keyik Annagulyyeva
#Advised by Jianghao Wang

import numpy as np
import random
import os
import time

#Displays my city

def Display_array(arr):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(arr[y][x], end='')
        print()
size = int(input("Enter a city size: "))
arr = np.full((size,size),'.')
population = 0
revenue = 0
a = 0.5

#Cash flood that updates the city to a dollar sign (can be considered a 'natural' disaster.) 

def Disaster(arr, population, revenue):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            arr[y][x] = '$'
        time.sleep(a)
        os.system('clear||cls')
        Display_array(arr)
    population -= 2
    revenue += 200000 
    return population, revenue 

#Monster that eats the part of the city (these monsters come once in a while as they get hungry)

def Disaster_upgrade(arr, population, revenue):
    y = random.randint(0, size - 2) 
    x = 0 
    for times in range(size - 1):
        arr[y][x] = '@'
        arr[y][x + 1] = '@'
        arr[y + 1][x] = '@'
        arr[y + 1][x + 1] = '@'
        x = x + 1
        time.sleep(a)
        os.system('clear||cls')
        Display_array(arr)
        arr[y][x - 1] = '.'
        arr[y + 1][x - 1] = '.'

    arr[y][x] = '.'
    arr[y][x - 1] = '.'
    arr[y + 1][x] = '.'
    arr[y + 1][x - 1] = '.'
    os.system('clear||cls')
    Display_array(arr) 
    population -= 2
    revenue -= 1000

#Turn the city back to '.' symbols, back to normal.

def clearDisaster(arr):
     for y in range(len(arr)):
        for x in range(len(arr[y])):
            arr[y][x] = '.'
        time.sleep(a)
        os.system('clear||cls')
        Display_array(arr)
    
#Allow the user to choose their own building.

def choose_building():
    options = ''' What would you like to build?

    1. HOUSE.
    2. FOUNTAIN.
    3. LIBRARY.
    4. BANK.
    5. RIVER.
    6. STREET.
'''
    print(options)
    user_building = input("Please choose a building (1/2/3/4/5/6): ")
    return user_building

#Define  each of my buildings, including the demolish feature of the game.

def house(arr,coord_y, coord_x, population, revenue):
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
        arr[coord_y][coord_x + 1] = "X"
        population -= 3
        revenue -= 5000
    else:    
        arr[coord_y][coord_x] = "["
        arr[coord_y][coord_x + 1] = "]"
        population += 10
        revenue += 10000
    return population, revenue 

def fountain(arr, coord_y, coord_x, population, revenue):
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
        population -= 2
        revenue -= 8000
    else:     
        arr[coord_y][coord_x] = "%"
        arr[coord_y][coord_x + 1 ] = "%"
        arr[coord_y + 1][coord_x] = "%"
        arr[coord_y + 1][coord_x + 1] = "%"
        population += 5
        revenue += 10500
    return population, revenue

def library(arr, coord_y, coord_x, population, revenue):
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
        population -= 8
        revenue -= 5200
    else:
        arr[coord_y][coord_x] = "#"
        arr[coord_y][coord_x + 1 ] = "#"
        arr[coord_y + 1][coord_x] = "#"
        arr[coord_y + 1][coord_x + 1] = "#"
        population += 5
        revenue += 10000
    return population, revenue

def bank(arr, coord_y, coord_x, population, revenue):
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
        population -= 10
        revenue += 5000
    else:
        arr[coord_y][coord_x] = "$"
        arr[coord_y][coord_x + 1 ] = "$"
        population += 10
        revenue += 20000
    return population, revenue

def river(arr, coord_y, coord_x):
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
    else:
        arr[coord_y][coord_x] = "~"
        arr[coord_y + 1 ][coord_x] = "~"
        arr[coord_y + 2 ][coord_x] = "~"
        
def street(arr, coord_y, coord_x):        
    if arr[coord_y][coord_x] != '.':
        arr[coord_y][coord_x] = "X"
    else:
        arr[coord_y][coord_x] = '='
        arr[coord_y][coord_x+1] = '='
        arr[coord_y][coord_x + 2] = '='

#Call out all of my previosus functions into the CityGame.

def cityGame(arr, population, revenue):
#Randomize the 'natural' disasters.
    disaster  = random.randint(0,4)
    if disaster == 0:
        population, revenue = Disaster(arr, population, revenue)
        clearDisaster(arr)
    elif disaster == 1:
        Disaster_upgrade(arr, population, revenue)
    else:
        Display_array(arr)
    
    if population < 0:
        population = 0
#Allow the user to quit the game.
    print()
    print("Revenue: $", revenue)
    print("Population: ", population)
    leave_the_city = input("Please type 'QUIT' if you want to quit.\nOr press anything on your keyboard to continue: ")
    print()
    if leave_the_city == "Quit" or leave_the_city == "quit":
        exit()
    user_building = choose_building()

#Promt the user to try again  if the input is out of size of the matrix or simply invalid.

    try:
        coord_y, coord_x = [int(i) for i in input("Please pick TWO coordinates: ").split()]
    except:
        print("Not correct input.")
        return population, revenue
    if coord_y > size or coord_x > size or coord_y < 0 or coord_x < 0:
        print("Input out of bounds.")
        return population, revenue
    user_building = user_building.strip()
    
    if user_building == "1":
        population, revenue = house(arr, coord_y, coord_x, population, revenue)
           
    elif user_building == "2":
        population, revenue = fountain(arr, coord_y, coord_x, population, revenue)

    elif user_building == "3":
        population, revenue = library(arr, coord_y, coord_x, population, revenue)
       
    elif user_building == "4":
        population, revenue = bank(arr, coord_y, coord_x, population, revenue)

    elif user_building  == "5":
        river(arr, coord_y, coord_x)
       
    else:
        street(arr, coord_y, coord_x)

    return population, revenue

#Main while loop within 10 lines of code.

while True:
    population, revenue =  cityGame(arr, population, revenue)
