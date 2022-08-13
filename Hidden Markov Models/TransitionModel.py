# Ben Lehrburger
# COSC 076 21F PA6

# Dependencies
import numpy as np
import copy
import random

# Make a transition model for the robot-maze problem
class TransitionModel:

    def __init__(self, maze, sensor_model):

        # Store the current maze
        self.maze = maze
        # Store the current sensor model
        self.sensor_model = sensor_model
        # 88% probability of correct reading
        self.sensor_accuracy = 0.88

    # get children of the current node
    def get_successors(self, state):

        # move one unit north
        north = (state[0], state[1] + 1)
        # move one unit south
        south = (state[0], state[1] - 1)
        # move one unit east
        east = (state[0] + 1, state[1])
        # move one unit west
        west = (state[0] - 1, state[1])

        states = [north, south, east, west]

        # add the robot's current position as a successor of itself
        successors = [state]

        # for each cardinal direction
        for direction in states:

            # add the robot as a valid successor if it is moving to a floor square
            if self.maze.is_floor(direction[0], direction[1]):
                successors.append(direction)

        return successors

    # Conduct a random walk of the robot in the maze with a predefined number of steps
    def walk(self, steps):

        # Retrieve the robot's starting location
        start = self.maze.start_location
        # Store color sensor observations as robot moves
        evidence = []
        # Store the robot's path in the maze
        path = [start]
        # Store the current state as the robot's starting location
        state = start

        # For each move in the maze
        for step in range(steps):

            # If not our start state
            if step is not 0:

                # Choose a random successor
                state = random.choice(self.get_successors(state))
                # Add that state to the robot's path
                path.append(state)

            # Retrieve the actual color of the floor at the current state
            floor_color = self.sensor_model.floor_colors[state]

            # Choose a random value
            random_value = random.random()

            # There is an 88% chance that the current sensor reading is correct
            if random_value < self.sensor_accuracy:
                evidence.append(floor_color)

            # Otherwise, there is a 12% chance that our sensor reading is incorrect
            else:
                # If incorrect, select a random color that is not the actual square color as our observation
                color_errors = copy.deepcopy(self.sensor_model.colors)
                color_errors.remove(floor_color)
                random_color = random.choice(color_errors)
                evidence.append(random_color)

        return evidence, path

    # Build the transition model
    def transition(self):

        # 16 x 16 matrix
        model = np.zeros((self.maze.height ** 2, self.maze.width ** 2))

        # For each square in the maze
        for x in range(self.maze.width):
            for y in range(self.maze.height):

                # Transform that square to the 16x16 model
                row = y + x * self.maze.width

                # Store equivalent confidence in each successor state
                for successor in self.get_successors((x, y)):
                    col = successor[1] + successor[0] * self.maze.width
                    model[row][col] += 0.25

        return model
