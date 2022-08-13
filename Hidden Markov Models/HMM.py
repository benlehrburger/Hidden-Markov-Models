# Ben Lehrburger
# COSC 076 21F PA6

# Dependencies
import numpy as np
from Maze import Maze
from SensorModel import SensorModel
from TransitionModel import TransitionModel
from Filter import Filter

FN = 'maze_with_walls.maz'

# Compute the HMM model
class HMM:

    def __init__(self, file):

        # Store the current maze
        self.maze = Maze(file)
        # Build and store the sensor model
        self.sensor_model = SensorModel(self.maze)
        self.sensor_model.build_sensor_model()
        # Build and store the transition model
        self.transition_model = TransitionModel(self.maze, self.sensor_model)
        # Initialize the filter given a maze, sensor model, and transition model
        self.filter = Filter(self.maze, self.sensor_model, self.transition_model.transition())

    # Main executable function
    def main(self):

        print('\nThe colors of the floor squares in the maze are:')
        print(self.sensor_model)

        print('\nThe current location of the robot in the maze is:\n')
        print(self.maze)

        # Store the random walk path and sensor readings at each step
        evidence, path = self.transition_model.walk(7)

        print('The path that the robot actually took is: ' + str(path) + '\n')

        np.set_printoptions(formatter={'float': '{: 0.1f}%'.format})

        # Initial probability of being at any open floor square in the maze
        probability = 1 / len(self.maze.floor_squares)

        # Initialize distribution in 4x4 matrix
        # Apply to wall squares too but cancel out erroneous values during matrix multiplication
        distribution = np.full((self.maze.width, self.maze.height), probability)

        index = 0

        # For the probability calculated at each open square
        for percept in evidence:

            # Pass parameters through the filter
            probability_matrix = self.filter.execute(distribution, percept)

            # Transform the matrix for printing
            state_estimation = np.transpose(np.fliplr(100 * np.array(probability_matrix).reshape(4, 4)))

            # Update and save the current step
            step = path[index]
            self.maze.robot_location = step

            print('The current location of the robot in the maze is: ' + str(step) + '\n')
            print(self.maze)
            print('After step ' + str(step) + ' the robots state estimation is: \n')
            print(state_estimation, '\n')

            # Update the new distribution model
            distribution = np.array(probability_matrix)
            index += 1

# Run the model
if __name__ == '__main__':
    model = HMM(FN)
    model.main()
