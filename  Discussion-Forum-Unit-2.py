def greet(name):  
    print(f"Hello, {name}!")

greet("Jahid")


# Calling with a value
greet("Bob")  

# Calling with a variable
person_name = "Charlie"
greet(person_name) 

# Calling with an expression
greet("D" + "ave")  


def add_numbers(a, b):
    result = a + b  
    return result

sum_value = add_numbers(5, 7)
print(sum_value)  


def square(number): 
    return number * number

square_value = square(4)
print(square_value)


x = 10  

def modify_x():
    x = 5  
    print(f"Inside function, x = {x}")

modify_x()
print(f"Outside function, x = {x}")
