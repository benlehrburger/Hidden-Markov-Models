# Ben Lehrburger
# COSC 076 21F PA6

# Dependencies
import numpy as np

# Make an HMM filter object for the robot-maze problem
class Filter:

    def __init__(self, maze, sensor_model, transition_model):

        # Store the maze object
        self.maze = maze
        # Store the sensor model
        self.sensor_model = sensor_model
        # Store the transition model
        self.transition_model = transition_model

    # Process the HMM filter
    def execute(self, previous_probability, observation):

        # Compute the transition probabilities
        transition = np.dot(self.transition_model, previous_probability.flatten())
        # Compute the state probability given our sensor model
        state = np.dot(self.sensor_model.sensor_model[observation], transition)
        # Normalize the model
        normalized_state = state / state.sum()

        # Return the normalized state
        return normalized_state
