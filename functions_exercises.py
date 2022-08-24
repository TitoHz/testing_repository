from ast import Str
from cgi import print_arguments

test_string = "I am in home and I am hungry"
test_list = [1, 0, 3, 0, 0, 5, 6, 7]


def lesser_or_greater_number(a, b):
    """
    Return the lesser number if both numbers are evens.
    Return the greater number if they aren't.
    """
    if (a and b) % 2 == 0:
        if a < b:
            return a
        else:
            return b 

    else:
        if a > b:
            return a
        else:
            return b


def old_macdonald(name):
    """
    Capitalizes the first and the fourth letter of a name
    """
    if len(name) > 3:
        print(name[:3].capitalize() + name[3:].capitalize())
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        print(name.capitalize())
        return name.capitalize()

def master_yoda(text):
    """
    Given a sentence, return a sentence with the words reversed
    e.g: ('I am home') --> 'home am I'
    """
    final_text = ""
    text_parsed = text.split(" ")
    for x in reversed(text_parsed):
        final_text += x
        final_text += " "

    print(final_text)
    return final_text

def count_primes(number):
    """
    COUNT PRIMES: Write a function that returns the *number* 
    of prime numbers that exist up to and including a given number   
    """
    primes = [2]
    if number < 2:
        return 0
    
    x = 3
    while x <= number:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    
    print(primes)
    return len(primes)

#cd C:\Users\cpenu\Documents\Python project 1\testing_repository\ 
#python3 functions_exercises.py


def spy_games(num_list):
    """
    SPY GAME: Write a function that takes in a list of integers
    and returns True if it contains 007 in order

    test_list = [1, 0, 0, 0, 0, 3, 0, 5, 6, 7]
    spy_game([1,0,2,4,0,5,7]) --> True
    spy_game([1,7,2,0,4,5,0]) --> False    
    """
    code = [0, 0, 7, "x"]
    for x in num_list:
        if x == code[0]:
            code.pop(0)
                 
    return len(code) == 1
        
def test():
    if spy_games([0, 0, 7, 0, 4, 5]) == True:
        print("yes sir")
    else:
        print("FALSE")
