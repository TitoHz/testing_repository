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
    newList = []
    a = len(name)
    for x in name:
        if name >= 4:
            print(x[0])
        
    
   
        
        

old_macdonald("anorlondor")



