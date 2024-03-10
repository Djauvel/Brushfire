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

# Instatiate an array to store each obstacle layer
obstacles = np.ndarray((cspace_array.shape[0],cspace_array.shape[1],np.max(cspace_array)+1))

#Separate each layer
for i in range(cspace_array.shape[0]-1):
    for j in range(cspace_array.shape[1]-1):
        #print(f"Dimensions: {cspace_array.shape}")
        #print(f"i: {i}, j: {j}")
        #print(f"cspace_array: {cspace_array[i,j]}")
        obstacles[i,j,cspace_array[i,j]] = cspace_array[i,j]



#Test print
filepath = "testOutput.txt"
np.savetxt(filepath, obstacles[:,:,2], fmt = "%d")