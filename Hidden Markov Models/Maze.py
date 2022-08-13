# Ben Lehrburger
# COSC 076 21F PA6

# Adapted from code provided in PA2

# Wrap a maze object
class Maze:

    def __init__(self, mazeFileName):

        # Open the maze file
        self.file = open(mazeFileName)

        # Store the robot's starting location
        self.start_location = None
        # Store the robot's current location
        self.robot_location = None
        # Store the width of the maze
        self.width = None
        # Store the height of the maze
        self.height = None
        # Store the floor squares in an array
        self.map = None
        # Store the colors assigned to each floor square
        self.color_map = []
        # Store each open floor square
        self.floor_squares = []
        # Store each wall square
        self.wall_squares = []

        # Save all global variables
        self.read_file()
        # Close the file
        self.file.close()

    # Parse the maze file's contents
    def read_file(self):

        # Store each line
        lines = []
        # Store the reverse of each line for printing
        reversed_lines = []

        # For each line in the maze file
        for line in self.file:

            line = line.strip()

            # Pass if the line has no contents
            if len(line) == 0:
                pass

            # If the line is where we define the starting location of the robot
            elif line[0] == "\\":

                # Save the robot's starting location
                params = line.split()
                x = int(params[1])
                y = int(params[2])
                self.start_location = (x, y)
                self.robot_location = (x, y)

            # Otherwise the line is a part of the maze; store it
            else:
                lines.append(line)
                reversed_lines.append(line[::-1])

        # Update global variables
        self.width = len(lines[0])
        self.height = len(lines)
        self.map = list("".join(lines))
        self.color_map = list("".join(reversed_lines))

        # For each square in the maze
        for r in range(0, self.height):
            for c in range(0, self.width):

                # Save floor squares as floor squares
                if self.is_floor(c, r):
                    self.floor_squares.append((c, r))

                # Save wall squares as wall squares
                else:
                    self.wall_squares.append((c, r))

    # Taken from PA2
    def index(self, x, y):
        return (self.height - y - 1) * self.width + x

    # Taken from PA2
    def is_floor(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False

        return self.map[self.index(x, y)] == "."

    # Taken from PA2
    def create_render_list(self):

        renderlist = list(self.map)

        for index in range(0, len(self.robot_location), 2):

            x = self.robot_location[index]
            y = self.robot_location[index + 1]

            renderlist[self.index(x, y)] = self.robotchar(0)

        return renderlist

    # Taken from PA2
    def robotchar(self, robot_number):
        return chr(ord("R") + robot_number)

    # Taken from PA2
    def __str__(self):

        renderlist = self.create_render_list()

        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                s+= renderlist[self.index(x, y)]

            s += "\n"

        return s
