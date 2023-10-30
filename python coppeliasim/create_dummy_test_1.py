import sim
import sys
sys.path.append('C:\\Users\\zlxan\\AppData\\Local\\Programs\\Python\\Python311\\lib\\site-packages')
import numpy as np
import math
import time

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
#Get handles for the Pioneer robot and its wheels
error, pioneer_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_oneshot_wait)
error, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

# [-0.2161087840795517, -0.27541384100914, 0.1386490911245346]
# Get Pioneer robot's postion
error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
print("Robot's Position:", robot_position)

#sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_streaming) # velocity = 2
#sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_streaming) # velocity = 2
 
# if error == sim.simx_return_ok:
#         sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_blocking) # velocity = 2
#         sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_blocking) # velocity = 2
#         error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
#         print("Robot's Position:", robot_position)


# def get_robot_position(clientID, robot_handle):
#     errorCode, position = sim.simxGetObjectPosition(clientID, robot_handle, -1, sim.simx_opmode_blocking)
#     if errorCode == sim.simx_return_ok:
#         return position
#     else:
#         return None
    
# def main():
#     robot_name = 'Pioneer_p3dx'  # Replace with the name of your robot in CoppeliaSim
#     errorCode, robot_handle = sim.simxGetObjectHandle(clientID, robot_name, sim.simx_opmode_blocking)
#     errorCode, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
#     errorCode, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)
#     if errorCode == sim.simx_return_ok:
#         sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_streaming) # velocity = 2
#         sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_streaming) # velocity = 2
#         while True:
#             position = get_robot_position(clientID, robot_handle)
#             if position:
#                 print(f"Robot Position: {position}")
#     else:
#         print(f"Failed to get the handle for {robot_name}")





# Define the target position
target_position = [1, 1, robot_position[2]]

# Move to the target position one axis at a time
while robot_position[0] < target_position[0] or robot_position[1] < target_position[1]:
    if robot_position[0] < target_position[0]:
        # Move in the x-direction
        sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot)
    else:
        # Stop moving in the x-direction
        sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_oneshot)
    error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
    print("Robot's Position:", robot_position)

# Move to the target position one axis at a time
while robot_position[0] < target_position[0]:
    # Move in the x-direction
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot)

    # Get the updated position
    error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)

while robot_position[1] < target_position[1]:
    # Move in the y-direction
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot)
    
    # Get the updated position
    res, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)




