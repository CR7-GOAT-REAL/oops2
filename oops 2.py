#class to convert string to uppercase
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter a string: ") 

    def print_string(self):
        print(self.str1.upper())


str1 = IOString()

str1.get_string()
str1.print_string()




#create an Employee class to define an object from a function

class Employee():
    #constructor
    def __init__(self):
      print("Employee created")
    #destructor
    def __del__(self):
      print("Employee deleted, destructor called")

def create_obj():
    print("Making an object...")
    e1 = Employee()
    print("Function end")
    return e1

print("Calling create_obj() function...")
#calling the function to create an object
obj = create_obj()
print("Program end")




#enumerate method 
class PairElements():
    def two_sum(self, nums, target):
      lookup = {}

    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup [target - num], i)
        lookup[num] = i

value = int(input("Enter the target value:"))
print(PairElements().two_sum((10,20,10,40,50,60,70), value))


