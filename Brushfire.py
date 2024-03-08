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
        entries = [float(entry) for entry in entries]

        cspace.append(entries)

cspace_array = np.array(cspace)

print(cspace_array.max())