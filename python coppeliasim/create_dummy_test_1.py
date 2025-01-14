import sim
import sys
import numpy as np
import math
import time
import random

#initialize
pi = math.pi
# Define robot-specific parameters
wheel_distance = 0.33  # Distance between the wheels (adjust for your robot)
wheel_radius = 0.195  # Radius of the wheels (adjust for your robot)
# Calculate the required wheel velocities
wheel_speed = 1  # Adjust the speed as needed

# https://www.coppeliarobotics.com/helpFiles/en/legacyRemoteApiOverview.htm
# Connect to the CoppeliaSim server
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
sim.simxSynchronous(clientID, True) # synchronous mode
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
# #Get handles for the Pioneer robot and its wheels
# error, pioneer_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_oneshot_wait)
# error, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
# error, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

# # Get Pioneer robot's postion
# error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
# # print("Robot's Position:", robot_position)

# # Define the target position
# target_position = [1, 1, robot_position[2]]
# tolerance = 0.05 # set the tolerance

# # Move to the target position one axis at a time
# while (abs(target_position[0]-robot_position[0]) > tolerance):

#     # Move in the x-direction
#     sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot)
#     sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot)
#     # get current Pioneer robot's postion
#     error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
#     print("Robot's Position:", robot_position)


# # Stop moving in the x-direction
# sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_oneshot)
# sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_oneshot)

# ##################################################################################################################################

# # Turn the robot by a specified angle
# ##################################################################################################################################
# target_angle = math.radians(180) # Turn by 180 degrees
# print(target_angle)
# # Define robot-specific parameters
# wheel_distance = 0.33  # Distance between the wheels (adjust for your robot)
# wheel_radius = 0.195  # Radius of the wheels (adjust for your robot)
# # Calculate the required wheel velocities
# wheel_speed = 1  # Adjust the speed as needed
# angular_velocity = wheel_speed / wheel_radius
# inner_wheel_velocity = -angular_velocity * (wheel_distance / 2)
# outer_wheel_velocity = angular_velocity * (wheel_distance / 2)

# # Initialize current_orientation to a starting value
# current_orientation = [0.0, 0.0, 0.0]  # Assuming a starting orientation of [0.0, 0.0, 0.0]

# # Control loop to monitor the robot's orientation
# while abs(current_orientation[2] - target_angle) > tolerance:
#     sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_streaming)
#     sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_streaming)
#     sim.simxSynchronousTrigger(clientID)

#     _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
#     current_orientation_degrees = [math.degrees(angle) for angle in current_orientation]
#     print("Robot's Orientation (Degrees):", current_orientation_degrees)

# # Stop moving
# print("stop")
# while abs(current_orientation[2] - target_angle) < tolerance:
#     sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_streaming)
#     sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_streaming)
#     sim.simxSynchronousTrigger(clientID)

#     _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
#     current_orientation_degrees = [math.degrees(angle) for angle in current_orientation]
#     print("Robot's Orientation (Degrees):", current_orientation_degrees)
# print("stop complete")

# Generate a random dummy node in the grid
# ##################################################################################################################################
# Define random position for the dummy
x_points = [x * 0.5 for x in range(2, -6, -1)]  # From 2 to -2.5 with a step of -0.5
y_points = [y * 0.5 for y in range(-2, 6)]      # From -2 to 2.5 with a step of 0.5

# Select a random grid point
x = random.choice(x_points)
y = random.choice(y_points)
z = 0  # Assuming the grid is on the ground plane

random_dummy = [x, y, z]
random_dummy = [-2, 2, z]

# Create the dummy
ret, dummyobject = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)

if ret == sim.simx_return_ok:
    # Set the position of the dummy
    sim.simxSetObjectPosition(clientID, dummyobject, -1, random_dummy, sim.simx_opmode_blocking)
else:
    print('Failed to create a dummy')

# Move the Robot to the Dummy Node
# ##################################################################################################################################
#Get handles for the Pioneer robot and its wheels
error, pioneer_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx', sim.simx_opmode_oneshot_wait)
error, left_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error, right_motor_handle = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

# Get Pioneer robot's postion
error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
print("Robot's Position:", robot_position)

_, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
print("Robot's Orientation:", current_orientation)
# current_orientation_degrees = [math.degrees(angle) for angle in current_orientation]
# print("Robot's Orientation (Degrees):", current_orientation_degrees)

radian_tolerance = 1 * (pi / 180)  # 5 degrees tolerance (0.08727 radians)
distance_tolerance = 0.05  # set the tolerance 0.05 from dummy position 
tolerance = 0.5

# Calculate differences
dx = x - robot_position[0]
dy = y - robot_position[1]

# Calculate the angle in radians
target_angle = math.atan2(dy, dx)
print("Angle to the point (in radians):", target_angle)

while abs(current_orientation[2] - target_angle) >= radian_tolerance:
    # rotate robot to the right angle
    print("current orientation",current_orientation[2])
    print(current_orientation[2] > target_angle)
    print("hi")
    print(current_orientation[2] < target_angle)
    if current_orientation[2] > target_angle:
        # Clockwise Rotation
        angular_velocity = wheel_speed / wheel_radius
        inner_wheel_velocity = angular_velocity * (wheel_distance / 2)
        outer_wheel_velocity = -angular_velocity * (wheel_distance / 2)
        sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_streaming) 
        sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_streaming)
        sim.simxSynchronousTrigger(clientID)  # synchronously update 
        _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
        print(current_orientation)

    if current_orientation[2] < target_angle:
        # Counter-clockwise Rotation
        angular_velocity = wheel_speed / wheel_radius
        inner_wheel_velocity = -angular_velocity * (wheel_distance / 2)
        outer_wheel_velocity = angular_velocity * (wheel_distance / 2)
        sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_streaming) 
        sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_streaming)
        sim.simxSynchronousTrigger(clientID)  # synchronously update  
        _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
        print(current_orientation)
        
    else:
        while abs(current_orientation[2] - target_angle) < radian_tolerance:
            sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_streaming)
            sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_streaming)
            sim.simxSynchronousTrigger(clientID)
            _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
 
while True:
    sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0, sim.simx_opmode_oneshot)
    sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0, sim.simx_opmode_oneshot)

# while (dx**2+dy**2) >= tolerance**2:
#     _, current_orientation = sim.simxGetObjectOrientation(clientID, pioneer_handle, -1, sim.simx_opmode_streaming)
#     #current_orientation_degrees = [math.degrees(angle) for angle in current_orientation]
#     # check angle
#     while current_orientation[2] - target_angle >= radian_tolerance:
#         # rotate robot to the right angle
#         if current_orientation > target_angle:
#             # Clockwise Rotation
#             angular_velocity = wheel_speed / wheel_radius
#             inner_wheel_velocity = angular_velocity * (wheel_distance / 2)
#             outer_wheel_velocity = -angular_velocity * (wheel_distance / 2)
#             sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_streaming) 
#             sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_streaming)
#             sim.simxSynchronousTrigger(clientID)  # synchronously update 
#         else:
#             # Counter-clockwise Rotation
#             angular_velocity = wheel_speed / wheel_radius
#             inner_wheel_velocity = -angular_velocity * (wheel_distance / 2)
#             outer_wheel_velocity = angular_velocity * (wheel_distance / 2)
#             sim.simxSetJointTargetVelocity(clientID, left_motor_handle, inner_wheel_velocity, sim.simx_opmode_streaming) 
#             sim.simxSetJointTargetVelocity(clientID, right_motor_handle, outer_wheel_velocity, sim.simx_opmode_streaming)
#             sim.simxSynchronousTrigger(clientID)  # synchronously update              
#     sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 2, sim.simx_opmode_oneshot)
#     sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 2, sim.simx_opmode_oneshot)
#     # get current Pioneer robot's postion
#     error, robot_position = sim.simxGetObjectPosition(clientID, pioneer_handle, -1, sim.simx_opmode_blocking)
#     print("Robot's Position:", robot_position)
#     dx = x - robot_position[0]
#     dy = y - robot_position[1]

# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)

