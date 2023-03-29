import sim
import sys
import numpy as np

# Connect to the CoppeliaSim server
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID == -1:
    print('Failed to connect to CoppeliaSim')
    sys.exit()

##################################################################################################################################
# dummyall = [] # all dummy nodes store in a list
# rel_node_loc_x = 0  # initializatin location x

# Define the dimensions of the grid
x_dim = len(np.arange(2, -2.5, -0.5))
y_dim = len(np.arange(-2, 2.5, 0.5))

# Create a 2D list to hold the dummy objects
dummyall = [[None for y in range(y_dim)] for x in range(x_dim)]

# Define the starting position of the first dummy
rel_node_loc_x = 0

class dummyHandle_object:
    def __init__(self,rel_node_loc_x,rel_node_loc_y,dummyHandle):
        self.gridx = rel_node_loc_x
        self.gridy = rel_node_loc_y
        self.dummyHandle = dummyHandle
        
# for j in np.arange(2, -2.5, -0.5):
#     rel_node_loc_x += 1
#     rel_node_loc_y = 0
#     for i in np.arange(-2, 2.5, 0.5):
#         rel_node_loc_y += 1
#         # Create a dummy object in the simulation
#         ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
#         if ret == sim.simx_return_ok:
#             # Set the position of the dummy to define the position of the cuboid
#             ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [i, j, 0], operationMode=sim.simx_opmode_blocking)
#             if ret == sim.simx_return_ok:
#                 # Set the orientation of the dummy to define the orientation of the cuboid
#                 ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
#                 if ret == sim.simx_return_ok:
#                     # Create the cuboid using the dummy as a reference
#                     ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
#                     if ret == sim.simx_return_ok:
#                         current_node = dummyHandle_object(rel_node_loc_x,rel_node_loc_y,dummyHandle)
#                         dummyall.append(current_node)
#                         # print(current_node.gridx, current_node.gridy)
#                         print("Cuboid created successfully.")
#                     else:
#                         print("Error creating cuboid.")
#                 else:
#                     print("Error setting dummy orientation.")
#             else:
#                 print("Error setting dummy position.")
#         else:
#             print("Error creating dummy.")

# print(dummyall[1])


# Loop through the grid and create the dummy objects (i, j) refers to the relative locations (starting from (0, 0)), (x, y) refers to the absoltue location
for i, x in enumerate(np.arange(2, -2.5, -0.5)):
    for j, y in enumerate(np.arange(-2, 2.5, 0.5)):
        # Create a dummy object in the simulation
        ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
        if ret == sim.simx_return_ok: # Set the position of the dummy to define the position of the cuboid
            ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [x, y, 0], operationMode=sim.simx_opmode_blocking)
            if ret == sim.simx_return_ok: # Set the orientation of the dummy to define the orientation of the cuboid
                ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
                if ret == sim.simx_return_ok: # Create the cuboid using the dummy as a reference
                    ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
                    if ret == sim.simx_return_ok: 
                        current_node = dummyHandle_object(i, j, dummyHandle)# Create a dummyHandle_object to hold information about the dummy
                        dummyall[i][j] = current_node # Add the dummyHandle_object to the 2D list
                        print("Cuboid created successfully.")
                    else:
                        print("Error creating cuboid.")
                else:
                    print("Error setting dummy orientation.")
            else:
                print("Error setting dummy position.")
        else:
            print("Error creating dummy.")

def create_neignbor_links(dummyall):            
    for i in range(x_dim):
        for j in range(y_dim):
            obj = dummyall[i][j]
            if i > 0:
                left_neighbor = dummyall[i-1][j]
                obj.neighbors.append(left_neighbor)
            if i < x_dim-1:
                right_neighbor = dummyall[i+1][j]
                obj.neighbors.append(right_neighbor)
            if j > 0:
                up_neighbor = dummyall[i][j-1]
                obj.neighbors.append(up_neighbor)
            if j < y_dim-1:
                down_neighbor = dummyall[i][j+1]
                obj.neighbors.append(down_neighbor)
    print(dummyall[0][0].neighbors)

# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)
