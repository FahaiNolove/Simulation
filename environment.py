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
dummyall = [] # all dummy nodes store in a list
rel_node_loc_x = 0  # initializatin location x

class dummyHandle_object:
    def __init__(self,rel_node_loc_x,rel_node_loc_y,dummyHandle):
        self.gridx = rel_node_loc_x
        self.gridy = rel_node_loc_y
        self.dummyHandle = dummyHandle
        
for j in np.arange(2, -2.5, -0.5):
    rel_node_loc_x += 1
    rel_node_loc_y = 0
    for i in np.arange(-2, 2.5, 0.5):
        rel_node_loc_y += 1
        # Create a dummy object in the simulation
        ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
        if ret == sim.simx_return_ok:
            # Set the position of the dummy to define the position of the cuboid
            ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [i, j, 0], operationMode=sim.simx_opmode_blocking)
            if ret == sim.simx_return_ok:
                # Set the orientation of the dummy to define the orientation of the cuboid
                ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
                if ret == sim.simx_return_ok:
                    # Create the cuboid using the dummy as a reference
                    ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
                    if ret == sim.simx_return_ok:
                        current_node = dummyHandle_object(rel_node_loc_x,rel_node_loc_y,dummyHandle)
                        dummyall.append(current_node)
                        # print(current_node.gridx, current_node.gridy)
                        print("Cuboid created successfully.")
                    else:
                        print("Error creating cuboid.")
                else:
                    print("Error setting dummy orientation.")
            else:
                print("Error setting dummy position.")
        else:
            print("Error creating dummy.")

# print(dummyall[1])


def create_neignbor_links(dummyall):
    #for i,element in enumerate(dummyall):
    for obj in dummyall:
        # check left side
        if obj.gridx - 1 > 0:
            obj.neignbors.append(dummyall[obj.gridx - 1],[obj.gridy])
        # check right side
        if obj.gridx - 1 > 0:
            obj.neignbors.append(dummyall[obj.gridx + 1],[obj.gridy])
        # check up side
        if obj.gridx - 1 > 0:
            obj.neignbors.append(dummyall[obj.gridx],[obj.gridy + 1])
        # check down side
        if obj.gridx - 1 > 0:
            obj.neignbors.append(dummyall[obj.gridx + 1],[obj.gridy - 1])
    print(dummyall[0].neignbors)

# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)