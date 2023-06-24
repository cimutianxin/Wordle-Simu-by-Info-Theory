# Wordle Simulation by Infomation Theory

 Wordle, Infomation Theory, Information Entropy, Python

[wordle](https://wordlegame.org), a game that you guess a 5-letter word by the hint of the game.

Try to simulate the wordle game and find out the best way to guess, inspired by [3Blue1Brown's video](https://www.youtube.com/watch?v=v68zYyaEmEA).

- [x] Solution_0: use word has the highest E_info to guess every time.
- [x] Use short word list to generate the ANSWER and guess in the short word list, too.
- [x] The 1000-time-simulation shows that 'saner', which has highest E_info, is not the best choice(3.78 on aver). 'slate' gets 3.07 score, which is better.
- [ ] Haven't use the long word list to guess and calculate the E_info again at every guess. (I tried but it's too slow)
- [ ] Haven't use the frequency word list to calculate weighted information entropy. (I think it's a cheat in some way)
