import matplotlib as plt
import numpy as np

# Initialize an empty list to store the configuration space
cspace = []

# Parse cspace txt and save in memory
with open("cspace_low_res.txt", "r") as file:
    # Read each line in the file
    for line in file:
        # Split the line into individual entries
        entries = line.split()

        # Convert entries into floats
        entries = [int(float(entry)) for entry in entries]

        cspace.append(entries)
# Convert cspace nested lists to a numpy array
# Remove all float notation
cspace_array = np.round(np.array(cspace)).astype(int)

def voronoi(obstacles):
    # This function should contain the Brushfire algorithm implementation
    # The function will take an array of values that represent the configuration 
    # space and associated obstacles
    # Dimensions identical to the source cpsace array, but with 3 dimensions
    dimensions = (obstacles.shape[0], obstacles.shape[1], np.max(obstacles)+1)

    # Instatiate an array to store each obstacle layer
    obstacle_layers = np.zeros(dimensions)

    #Separate each layer
    for i in range(obstacles.shape[0]):
        for j in range(obstacles.shape[1]):
            if obstacles[i,j] != 0:
                obstacle_layers[i,j,obstacles[i,j]] = 1

    voronoi_array = np.array()

    return voronoi_array




#Test print
#filepath = "testOutput.txt"
#np.savetxt(filepath, obstacles[:,:,1], fmt = "%d")