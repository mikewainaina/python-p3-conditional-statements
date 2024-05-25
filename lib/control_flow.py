#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username =="SDFT-09" and password =="Moringa":
       return "Welcome dear user"

    elif username =="SDFT-09" and password =="Moringa":
        return "Welcome dear user"
    else:
        return "Invalid username or password"
    
    pass
    
def hows_the_weather(temperature):
    # your code here
    if temperature <63:
        return "It's cold!!"
    
    elif temperature >=64 and temperature >89:
        return "It's terribly hot!!"
    else:
        return "It's nice and warm!!"
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
    print ("Syntax error in the calculation!!")
    return none
    pass
