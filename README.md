
# Adversarial Game Playing Agent on "Isoloation" 

![Example game of isolation on a square board](viz.gif)

## What is this? 

This is a simple agent to play "Isolation" game. 



## About "Isolation" Game 

In the game Isolation, two players each control their own single token and alternate taking turns moving the token from one cell to another on a rectangular grid.  Whenever a token occupies a cell, that cell becomes blocked for the remainder of the game.  An open cell available for a token to move into is called a "liberty".  The first player with no remaining liberties for their token loses the game, and their opponent is declared the winner.

In knights Isolation, tokens can move to any open cell that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board.  On a blank board, this means that tokens have at most eight liberties surrounding their current location.  Token movement is blocked at the edges of the board (the board does not wrap around the edges), however, tokens can "jump" blocked or occupied spaces (just like a knight in chess).

Finally, agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond.  The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move.

**You can find more information (including implementation details) about the in the Isolation library readme [here](/isolation/README.md).**

## The algorithm 

  - Used a simple heuristic the score is evaluated as  sum(distances from player's available spaces to the position of the opponent) / sum (distances from opponent's available spaces to the position of the player )
  - This wins against MINIMAX algorithm with more than 60% of matches 

## How to Run? 

- after downloading this repository, run 'python run_match.py'
- there are some arguments accepted
    - -r + int : specify the number of rounds 
    - -o + (RANDOM or GREEDY or MINIMAX): choose the opponent
    - -f : play in fair mode
    - -t + int:  settime limit in miliseconds 
- player's algorithm is written in 'my_custom_player.py' 
