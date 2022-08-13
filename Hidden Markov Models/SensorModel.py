# Ben Lehrburger
# COSC 076 21F PA6

# Dependencies
import random
import numpy as np

# Make a sensor model for the robot-maze problem
class SensorModel:

    def __init__(self, maze):

        # Store the maze object
        self.maze = maze
        # Store the available floor colors
        self.colors = ['r', 'g', 'b', 'y']
        # Initialize dictionary with key as coordinate and value as color
        self.floor_colors = {}
        # Initialize dictionary with key as color and value as 1x16 matrix of color's value at each coordinate
        self.sensor_model = {}
        # 88% probability of correct reading
        self.sensor_accuracy = 0.88
        # 4% chance of reading each color incorrectly
        self.sensor_error = 0.04

    # Get the color of a floor tile
    def get_color(self, x, y):
        return self.floor_colors[(x, y)]

    # Build the sensor model
    def build_sensor_model(self):

        # Get the mapping of each floor square
        self.maze.color_map.reverse()

        # For each square in the maze
        for square in self.maze.floor_squares:

            # Assign a random color
            color = random.choice(self.colors)
            self.floor_colors[square] = color

            # Transform the current floor square to the color mapping for printing
            index = square[0] + self.maze.width * square[1]
            self.maze.color_map[index] = color

        # For each available floor color
        for color in self.colors:

            # Initialize a 1x16 vector
            color_model = np.identity(self.maze.width ** 2)
            index = 0

            # For each floor square
            for x in range(self.maze.width):
                for y in range(self.maze.height):

                    # If the square is not a wall
                    if self.maze.is_floor(x, y):

                        # If the floor square is the current color
                        if self.get_color(x, y) == color:
                            # We have an 88% probability of reading that color correctly
                            color_model[index][index] = self.sensor_accuracy
                        else:
                            # We have a 0.04 probability of reading that color incorrectly
                            color_model[index][index] = self.sensor_error

                    else:
                        # If it's a wall our color reading is 0
                        color_model[index][index] = 0

                    # Increment index
                    index += 1

            # Add each color's matrix to the sensor model
            self.sensor_model[color] = color_model

    # To string method for printing the color model
    def __str__(self):

        renderlist = self.maze.color_map

        s = ""
        for y in range(self.maze.height - 1, -1, -1):
            string = ""
            for x in range(self.maze.width):
                string += renderlist[self.maze.index(x, y)]
            s += string[::-1]

            s += "\n"

        return s[::-1]
