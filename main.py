# Path: main.py
# This is the main file that will be run. 
# This file will import the greet.py file and use the Greet class to say hello and tell the age of the user..

from greet import Greet

greet = Greet()

greet.say_hello()
print(greet.tell_age())