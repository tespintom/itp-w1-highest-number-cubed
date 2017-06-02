"""This is the entry point of the program."""

'''
def highest_number_cubed(limit):
    i = 0
    for i in limit:
        if i ** 3 < limit:
            return i + 1
        else:
            return i - 1
'''

def highest_number_cubed(limit):
    number = 0 #make this outside the loop for not to reset.  
    
    while True:
        number += 1
        if number ** 3 > limit:
            return number -1
        
'''
def highest_number_cubed(limit):
    number = 0
    for number in limit:
        number += 1
        if number ** 3 > limit:
            return number - 1
            
'''            