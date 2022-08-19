from ast import Str

test_string = "I am in home and I am hungry"
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
            print(y)
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    
    print(primes)
    return len(primes)

count_primes(15)




