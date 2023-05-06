import sim
import sys
import numpy as np
import math

# Connect to the CoppeliaSim server
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID == -1:
    print('Failed to connect to CoppeliaSim')
    sys.exit()

amr_name = 'amr_name' # Replace with the desired name for the AMR object
amr_size = [0.5, 0.5, 0.2] # Replace with the desired size of the AMR (x, y, z)
amr_position = [0, 0, 0.1] # Replace with the desired initial position of the AMR (x, y, z)

res, amr_handle = sim.simxCreateDummy(clientID, size=0.1, color=None, operationMode=sim.simx_opmode_blocking) # Create the AMR object
if res != sim.simx_return_ok:
    print("Failed to create AMR")
    exit()
#ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
sim.simxSetObjectPropertyString(clientID, amr_handle, amr_name, sim.simx_opmode_blocking) # Set the name of the AMR object
sim.simxSetObjectPosition(clientID, amr_handle, -1, amr_position, sim.simx_opmode_blocking) # Set the initial position of the AMR object

# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)
