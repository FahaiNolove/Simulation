import sim
import sys
import numpy as np
import math
import time

# https://www.coppeliarobotics.com/helpFiles/en/legacyRemoteApiOverview.htm
# Connect to the CoppeliaSim server
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID == -1:
    print('Failed to connect to CoppeliaSim')
    sys.exit()

# create dummy nodes
##################################################################################################################################
# # Define the dimensions of the grid
# x_dim = len(np.arange(2, -2.5, -0.5))
# y_dim = len(np.arange(-2, 2.5, 0.5))

# # Create a 2D list to hold the dummy objects
# dummyall = [[None for y in range(y_dim)] for x in range(x_dim)]

# # Define the starting position of the first dummy
# rel_node_loc_x = 0

# class dummyHandle_object:
#     def __init__(self,rel_node_loc_x,rel_node_loc_y,dummyHandle):
#         self.name= "node(" + str(i) + "," + str(j) + ")"
#         self.gridx = rel_node_loc_x
#         self.gridy = rel_node_loc_y
#         self.dummyHandle = dummyHandle
#         self.neighbors=[]


# # Loop through the grid and create the dummy objects (i, j) refers to the relative locations (starting from (0, 0)), (x, y) refers to the absoltue location
# for i, x in enumerate(np.arange(2, -2.5, -0.5)):
#     for j, y in enumerate(np.arange(-2, 2.5, 0.5)):
#         # Create a dummy object in the simulation
#         ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
#         if ret == sim.simx_return_ok: # Set the position of the dummy to define the position of the cuboid
#             ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [x, y, 0], operationMode=sim.simx_opmode_blocking)
#             if ret == sim.simx_return_ok: # Set the orientation of the dummy to define the orientation of the cuboid
#                 ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
#                 if ret == sim.simx_return_ok: # Create the cuboid using the dummy as a reference
#                     ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
#                     if ret == sim.simx_return_ok: 
#                         current_node = dummyHandle_object(i, j, dummyHandle)# Create a dummyHandle_object to hold information about the dummy
#                         dummyall[i][j] = current_node # Add the dummyHandle_object to the 2D list
#                         print("Cuboid created successfully.")
#                     else:
#                         print("Error creating cuboid.")
#                 else:
#                     print("Error setting dummy orientation.")
#             else:
#                 print("Error setting dummy position.")
#         else:
#             print("Error creating dummy.")

# def create_neignbor_links(dummyall):            
#     for i in range(x_dim):
#         for j in range(y_dim):
#             obj = dummyall[i][j]
#             if i > 0:
#                 left_neighbor = dummyall[i-1][j]
#                 obj.neighbors.append(left_neighbor)
#             if i < x_dim-1:
#                 right_neighbor = dummyall[i+1][j]
#                 obj.neighbors.append(right_neighbor)
#             if j > 0:
#                 up_neighbor = dummyall[i][j-1]
#                 obj.neighbors.append(up_neighbor)
#             if j < y_dim-1:
#                 down_neighbor = dummyall[i][j+1]
#                 obj.neighbors.append(down_neighbor)

# create_neignbor_links(dummyall)
# print([n.name for n in dummyall[0][0].neighbors])

##################################################################################################################################

# let AMR follows a path
##################################################################################################################################
 # Get handles for the Pioneer robot and its wheels
error, pioneer_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_oneshot_wait)
error, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

# Drive the robot forward for 5 seconds
sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_blocking) # velocity = 2
sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_blocking) # velocity = 2

# sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot) # velocity = 2
# sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot) # velocity = 2
# time.sleep(1)


# Turn the robot by a specified angle
target_angle = math.pi/4 # Turn by 45 degrees
turn_radius = 0.2 # Radius of the turn
wheel_distance = 0.33 # Distance between the wheels
turn_speed = 1.0 # Speed of the turn

# Calculate the required wheel velocities to turn the robot
inner_wheel_velocity = turn_speed * (turn_radius - (wheel_distance/2))
outer_wheel_velocity = turn_speed * (turn_radius + (wheel_distance/2))

# Set the wheel velocities to turn the robot
if target_angle > 0:
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_oneshot)
else:
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, outer_wheel_velocity, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, inner_wheel_velocity, sim.simx_opmode_oneshot)

# # Wait for the robot to turn to the desired angle
# current_angle = 0
# while abs(current_angle) < abs(target_angle):
#     # Get the current orientation of the robot
#     error, orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
    #current_angle = orientation[2]

# orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
# # Turn the robot 90 degrees
# sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 1, sim.simx_opmode_oneshot)
# sim.simxSetJointTargetVelocity(clientID, right_motor_handle, -1, sim.simx_opmode_oneshot)
# #time.sleep(int(math.radians(90) / 1))

# # Stop the robot
# sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_oneshot)
# sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_oneshot)

#amr_name = 'PioneerP3DX'
# amr_name = 'Cuboid'
# res, amr_handle = sim.simxGetObjectHandle(clientID, amr_name, sim.simx_opmode_blocking) # Get the AMR's handle
# if res != sim.simx_return_ok:
#     print("Failed to get AMR handle")
#     exit()

# path_coordinates = [(0, 0), (1, 1), (2, 2)]

# for coord in path_coordinates:
#     target_x = coord[0] # Extract x-coordinate from path
#     target_y = coord[1] # Extract y-coordinate from path

#     # Calculate the target angle for the AMR to face the next waypoint
#     current_x, current_y, _ = sim.simxGetObjectPosition(clientID, amr_handle, -1, sim.simx_opmode_blocking)[1]
#     dx = target_x - current_x
#     dy = target_y - current_y
#     target_angle = math.atan2(dy, dx)

#     # Set the target angle for the AMR to face
#     sim.simxSetObjectOrientation(clientID, amr_handle, -1, [0, 0, target_angle], sim.simx_opmode_blocking)

#     # Move the AMR towards the next waypoint
#     sim.simxSetObjectPosition(clientID, amr_handle, -1, [target_x, target_y, 0.1], sim.simx_opmode_blocking)

#     # Wait for the AMR to reach the target position
#     while True:
#         current_x, current_y, _ = sim.simxGetObjectPosition(clientID, amr_handle, -1, sim.simx_opmode_blocking)[1]
#         if math.sqrt((current_x - target_x) ** 2 + (current_y - target_y) ** 2) < 0.1:
#             break

# print("AMR reached the end of the path.")


# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)
