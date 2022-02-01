#Object Oriented Programming
#__init__:  init is a method or function that is going to automatically be called every time that I try to 
#create a new point.  And this function takes a couple of arguments.
#All functions that operate on objects themselves, otherwise known as methods, are going to take the first 
#argument called self and this argument self represents the object in question.
# 


class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)


"""
Explanation: 
Let's define a new class that we're going to call flight. And this time the init is going to take a single 
argument other than the selfm which is the capacity. 

So I'll store that inside of a value called self.capacity equals capacity. And we create a list and saved
passengers which is an empty list.

NEW ADD_PASSENGER METHOD : when we add a passenger we added by the name .

We stote passengers in self.passengers and this is a list and we add with append(name).

NEW OPEN_SEATS , we need return capacity minus.self passengers

"""

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry","Ron","Hermione","Ginny"]

for person in people: 
    success = flight.add_passenger(person)
    if success: 
        print(f"Added {person} to flight successfully.")
    else: 
        print(f"No available seats for {person}")