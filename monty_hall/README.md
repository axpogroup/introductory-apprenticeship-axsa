# The Monty Hall Problem
The Monty Hall problem is a famous probability puzzle based on a game show scenario. 
It is named after Monty Hall, the original host of the television game show "Let's Make a Deal."

## Problem Description
In the Monty Hall problem, a contestant is presented with three doors:
1. Behind one door is a car (the prize the contestant wants).
2. Behind the other two doors are goats (which the contestant does not want).
3. The contestant picks one of the three doors (but does not open it yet).
4. The host, who knows what is behind each door, opens one of the remaining two doors, revealing a goat.
5. The contestant is then given the option to either stick with their original choice or switch to the other unopened door.
6. The contestant's goal is to maximize their chances of winning the car.

## Task 1 – Understand the Rules (No Coding)
Write down the rules of the Monty Hall game in your own words:
1. There are 3 doors
2. One door has a car, two have goats
3. The player picks one door
4. The host:
   - knows where the car is
   - always opens a different door
   - always reveals a goat
   - the player may stay or switch

## Task 2 – Table‑Based Proof (Logic Proof, No Coding)

Create a table of all possible cases assuming:
- You always pick Door 1 
- The car is placed randomly

| Car Location  | Door Opened by Host | Stay Wins? | Switch Wins? | 
|---------------|---------------------|------------|--------------|
| Door 1        | ?                   | ?          | ?            |
| Door 2        | ?                   | ?          | ?            |
| Door 3        | ?                   | ?          | ?            |

How many times do you win if you always stay? 
How many times do you win if you always switch?


## Task 3 – First Coding Challenge (Single Game)

Write code that simulates one Monty Hall game.

Requirements:
- Randomly place the car
- Randomly choose a player door
- Host opens a goat door
- Player switches
- Return True if the player wi

## Task 4 – Simulation Proof (Core Challenge)
Write code that simulates 10,000 Monty Hall games and count wins when staying vs switching.
