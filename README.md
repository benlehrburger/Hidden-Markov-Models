# Hidden-Markov-Models

This program builds and computes a Hidden Markov Model for a robot in a 4x4 maze (although any dimensions can be used). Each square in the maze has an assigned color. The layout of the maze and the colors of the floor squares are known, but the robot's color sensor is faulty. The sensor has an 88% chance of reading the correct color and a 4% of guessing any other color incorrectly. Our task is to calculate the probability distribution of the robot being at any given position in the maze during a random walk.

My code is comprised of five files representing five subproblems. The code accepts a maze files and reads it, extracting the relevant features of the maze (size, floor squares, floor colors, etc). After building a maze object, the program then builds sensor and transition models. 

Each color has its own sensor model, where the probabilities of sensing that color at each square are stored. I built a 1x16 matrix for each color, with each index representing a floor square, and filled it with the probabilities of seeing that color at the present square. Again, there is an 88% chance of reading the color value correctly and a 4% chance of reading another value. To simulate this error probability, I retrieved a random number and returned the correct color if that number was less than 0.88, otherwise I returned some incorrect color.

The transition model defines how the robot's probability changes as it moves between states given new sensory information. I had the robot conduct a random walk, retrieving new sensory information and its eligible successors at each step, then choosing a random successor to subsequently move to. I stored equivalent confidence that the robot could be at each successor state since it doesn't know where it is in the maze for certain.

I then passed the sensor and transition models through my filter. It takes the dot produce of the transition model and the previous iteration's calculated probability. Initially, the probability distribution is equivalent across all open floor squares. It then takes that product and multiplies it with the sensor model for the observed color. Lastly, it normalizes the resulting matrix and returns it.

The main executable function of the program lies in the 'HMM.py' file. This file brings together the maze object, the sensor model, the transition model, and the filter to compute probability distributions at each successive step. The user has the option to specify their desired number of steps in the maze, along with the maze file that they would like to use.
