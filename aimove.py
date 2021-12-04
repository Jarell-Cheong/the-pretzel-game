''' Perform a move and program an AI to move '''


# Import relevant libraries
from random import randint


# Check if a move is valid
def valid(link, index, operation):

    if index not in range(0, len(link)):
        return False

    if operation not in [0, 1]:
        return False

    if operation == 1 and link[index] in [-1, 1]:
        return False

    return True


# Make a move given input parameters
def move(link, index, operation):

    if operation == 0:
        link.pop(index)

    else:
        if link[index] > 1:
            link[index] -= 1
        else:
            link[index] += 1

    return link
    

# Make a random AI move given a link
def ai_random(link):
    
    index = randint(0, len(link) - 1)
    
    operation = randint(0, 1)

    if valid(link, index, operation):
        return move(link, index, operation)

    else:
        return ai_random(link)


# Make the best AI move given a link
def ai_better(link):

    length = len(link)
    
    if length > 3:
        return ai_random(link)

    elif length == 3:
        for i in range(length):
            if link[i] > 1:
                return move(link, i, 1)
        return ai_random(link)

    else:
        return move(link, 0, 0)