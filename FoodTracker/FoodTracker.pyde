# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
import random

def setup():
    global vehicle, food, foodCounter
    size(2*640, 2*360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    foodCounter = 0 
    food = Food(random.randint(64, width), random.randint(64, height), PVector(0,0))
    textSize(16)

def draw():
    global foodCounter
    background(255)
    mouse = PVector(mouseX, mouseY)
    distance = PVector.dist(vehicle.position, food.position)
    print(distance)
    if distance < 1:
        print("close enougth")
        food.position = PVector(random.randint(64, width), random.randint(64, height))
        foodCounter =  foodCounter + 1
    else:
        print("too far")
        vehicle.velocity = (food.position - vehicle.position) / PVector.dist(food.position, vehicle.position)

    text("Counter: " + str(foodCounter), 10, 30)
    vehicle.update()
    vehicle.display()
    food.display()
