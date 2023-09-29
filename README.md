# TicTacToe
Aproject made for CS50AI Course 
**Tic-Tac-Toe (Minimax)** 

* The assignment is about writing an AI algorithm to play Tic-Tac-Toe optimally
* The pygame module provided inside the <code>runner.py</code> file was outside the scope of the project
* The solution is based on Minimax decision rule which perfectly works for games that clash two opponents against each other
    * The algorithm is all about calculating the best utility out of all possible solutions. 
    * The algorithm relies on calculating prospective steps that the opponent might take

* The <code>tictactoe.py</code> file (where the solution lies) consists of many minor functions that construct the game of Tic-Tac-Toe (finding out who is a winner, etc.)
I recommend paying better attention to the last function called <i>minimax</i>
    * The function determines which side AI plays for, and then finds the best optimal score that the AI can get

   ![tictactoe demo](demo/tictactoe.gif)
