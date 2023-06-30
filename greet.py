# This is the class that will be imported into the main.py file.
# This class will be used to greet the user and tell the age of the user.
# This class has two methods: say_hello and tell_age.

# The say_hello method will greet the user.
# The say_hello method will return a string.
# The say_hello method will return "Hello {name}" where {name} is the name of the user.

# The tell_age method will ask the user for their year of birth and tell them their age.
# The tell_age method will return a string.
# The tell_age method will return "Invalid input" if the user enters a non-numeric value.
# The tell_age method will return "Hey {name}, you are {age} years old" if the user enters a numeric value.


class Greet:
    def __init__(self):
        self.name = input("Enter your name: ")

    def say_hello(self):
        print(f"Hello {self.name}")
    
    def tell_age(self):
        dob = input("Enter your year of birth(YYYY): ")
        try:
            age = 2023-int(dob) 
            return(f"Hey {self.name}, you are {age} years old")
        except ValueError:
            return("Invalid input")
