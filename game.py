''' Play the game in the command line with the user '''


# Import relevant libraries
from random import randint, sample
from completion import check
from aimove import valid, move, ai_random, ai_better


# Generate a pretzel link
def generate():

    # Generate random parameters for the link
    length = randint(4, 10)
    values = [-x for x in range(1, 10)] + [x for x in range(1, 10)]

    return sample(values, length)


# Ask user for type of game
def new():

    # Ask for game type
    type = input("Would you like to play the random or better version? (r/b): ")

    # Play the game based on user response
    if type in ["r", "R"]:
        random_game()
    elif type in ["b", "B"]:
        better_game()
    else:
        print("Invalid game type.")


# Play the random version of the game
def random_game():
    
    # Generate the board
    link = generate()
    print("This will be the board.")
    print(link)

    while True:

        # Ask user for move
        index = int(input("Index: "))
        operation = int(input("Operation: "))

        # Play if user move is valid
        if valid(link, index, operation):
            
            # Make user move
            link = move(link, index, operation)
            print("The link after your move.")
            print(link)

            # Check if user has won
            if check(link):
                print("You have won!")
                break

            # Make AI move
            link = ai_random(link)
            print("AI has made their move.")
            print(link)

            # Check if AI has won
            if check(link):
                print("You have lost!")
                break

        # Reprompt user for move
        else:
            print("Invalid move. Try again.")

    # Ask if user wants to play again
    decision = input("Would you like to play again? (y/n): ")

    # Restart the game if yes
    if decision in ["y", "Y"]:
        new()

    # Quit the game otherwise
    else:
        print("Thanks for playing!")    


# Play the better version of the game
def better_game():
    
    # Generate the board
    link = generate()
    print("This will be the board.")
    print(link)

    while True:

        # Ask user for move
        index = int(input("Index: "))
        operation = int(input("Operation: "))

        # Play if user move is valid
        if valid(link, index, operation):
            
            # Make user move
            link = move(link, index, operation)
            print("The link after your move.")
            print(link)

            # Check if user has won
            if check(link):
                print("You have won!")
                break

            # Make AI move
            link = ai_better(link)
            print("AI has made their move.")
            print(link)

            # Check if AI has won
            if check(link):
                print("You have lost!")
                break

        # Reprompt user for move
        else:
            print("Invalid move. Try again.")

    # Ask if user wants to play again
    decision = input("Would you like to play again? (y/n): ")

    # Restart the game if yes
    if decision in ["y", "Y"]:
        new()

    # Quit the game otherwise
    else:
        print("Thanks for playing!")


# Execute the game under appropriate conditions
if __name__ == "__main__":
    new()