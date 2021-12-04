# Process

A summary of the process used in this design is provided below, but for a more in-depth explanations of the functions used in each file, view Section 2 of the provided expository paper at https://github.com/Jarell-Cheong/the-pretzel-game/blob/master/static/pretzel.pdf.

# Completion

This file contains the function `check` that detects whether a list representation of a pretzel link is in its fully simplified or not. It does so by expressing a list in normal form before appealing to the theorems in the given paper. Most helper functions use `for` loops and recursion to perform their expected tasks.

# AI Move

This file contains the functions `move`, `ai_random` and `ai_better`. `move` makes a move by altering the list representing the pretzel link, while `ai_random` and `ai_better` suggest the moves that are to be made by the computer, be it at random or with a simple algorithm that makes sensible moves as the game nears its end.

# Game

This file runs the main game. `if` statements are used throughout to ask the user for the game mode and for rematches once initial games are over. A main `while` loop keeps the game going, and the player and computer take turns making moves, with the `check` function checking for game completion after every move.

# App

This file runs the web app that contains the explanations and rules for the game. The Streamlit library is used for its ease in creating web apps that integrate well with Python. Included in the web app is a video demonstration and an explanation of key concepts with images.

# Challenges

This project had a much more ambitious goal at the start, and many features proved too difficult to be implemented in the given time frame. Knot visualization is particularly tricky, and none of the options among the ones considered, i.e. `wolframclient`, `sage`, `snappy`, or `latex`, worked well with the rest of the game.

Implementing the logic of the game in a web application was also a great challenge, and in hindsight, a package meant for games like `pygame` would have probably worked better in this use case. A minimax algorithm was also created, but errors in the logical structure of its code made its play rather questionable in practical situations.

# Future Goals

In the future, the following features will be added progressively.
- Visualization for each list as a pretzel link after each move.
- A web application where the game can be played interactively.
- Hosting for said web application on the cloud.
- A minimax algorithm that plays with a reasonable strength.
- Interactive 3D links that users can click on to make their moves.