# #Import Libraries:
# import sim                  #V-rep library
# import sys
# import time                #used to keep track of time
# import numpy as np         #array library
# import math
# import matplotlib as mpl   #used for image plotting
# import socket   #for send data function
# import time     #for send data function
# import struct   #for create cuboid function
# from ctypes import byref    #pass a variable by reference, rather than by value


# #Pre-Allocation

# PI=math.pi  #pi=3.14..., constant

# #connection
# sim.simxFinish(-1) # just in case, close all opened connections

# clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)

# if clientID!=-1:  #check if client connection successful
#     print ('Connected to remote API server')
#     # Create a dummy object in the simulation
#     ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
#     if ret == sim.simx_return_ok:
#         # Set the position of the dummy to define the position of the cuboid
#         ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [1, 1, 1], operationMode=sim.simx_opmode_blocking)
#         if ret == sim.simx_return_ok:
#             # Set the orientation of the dummy to define the orientation of the cuboid
#             ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
#             if ret == sim.simx_return_ok:
#                 # Create the cuboid using the dummy as a reference
#                 ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
#                 if ret == sim.simx_return_ok:
#                     print("Cuboid created successfully.")
#                 else:
#                     print("Error creating cuboid.")
#             else:
#                 print("Error setting dummy orientation.")
#         else:
#             print("Error setting dummy position.")
#     else:
#         print("Error creating dummy.")
#     #create_cuboid(clientID)
#     sim.simxFinish(clientID)  
# else:
#     print ('Connection not successful')
#     sys.exit('Could not connect')


import sim
import sys

# Connect to the CoppeliaSim server
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID == -1:
    print('Failed to connect to CoppeliaSim')
    sys.exit()


# # Create a dummy object
# # options = {
# #     'parentObjectHandle': 'ResizableFloor_5_25',
# #     'position': (0.1, 0.2, 0.3),
# #     'orientation': (0, 0, 0, 1)
# # }
# color = [255, 0, 0]  # Red

# res, dummy_handle = sim.simxCreateDummy(clientID, size=0.1, operationMode=sim.simx_opmode_blocking, color=color)

# # # Set the position of the dummy object
# # position = [1.0, 2.0, 3.0]  # Replace with the desired position
# # res = sim.simxSetObjectPosition(clientID, dummy_handle, -1, position, sim.simx_opmode_oneshot)
# if res == sim.simx_return_ok:
#     # Set the position of the dummy to define the position of the cuboid
#     ret = sim.simxSetObjectPosition(clientID, dummy_handle, -1, [1, 1, 1], operationMode=sim.simx_opmode_blocking)
#     if res == sim.simx_return_ok:
#         print('Dummy object created')
# else:
#     print('Failed to create dummy object')


    # Create a dummy object in the simulation
ret, dummyHandle = sim.simxCreateDummy(clientID, size=0.1, color=[255, 0, 0], operationMode=sim.simx_opmode_blocking)
if ret == sim.simx_return_ok:
    # Set the position of the dummy to define the position of the cuboid
    ret = sim.simxSetObjectPosition(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
    if ret == sim.simx_return_ok:
        # Set the orientation of the dummy to define the orientation of the cuboid
        ret = sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0, 0, 0], operationMode=sim.simx_opmode_blocking)
        if ret == sim.simx_return_ok:
            # Create the cuboid using the dummy as a reference
            ret, _, _, _, _ = sim.simxGetObjectGroupData(clientID, sim.sim_object_shape_type, 0, operationMode=sim.simx_opmode_blocking)
            if ret == sim.simx_return_ok:
                print("Cuboid created successfully.")
            else:
                print("Error creating cuboid.")
        else:
            print("Error setting dummy orientation.")
    else:
        print("Error setting dummy position.")
else:
    print("Error creating dummy.")
# Disconnect from the CoppeliaSim server
sim.simxFinish(clientID)
# #retrieve motor handles
# errorCode,left_motor_handle=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',sim.simx_opmode_oneshot_wait)
# errorCode,right_motor_handle=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',sim.simx_opmode_oneshot_wait)

# sensor_h=[] #empty list for handles
# sensor_val=np.array([]) #empty array for sensor measurements

# #orientation of all the sensors: 
# sensor_loc=np.array([-PI/2, -50/180.0*PI,-30/180.0*PI,-10/180.0*PI,10/180.0*PI,30/180.0*PI,50/180.0*PI,PI/2,PI/2,130/180.0*PI,150/180.0*PI,170/180.0*PI,-170/180.0*PI,-150/180.0*PI,-130/180.0*PI,-PI/2]) 

# #for loop to retrieve sensor arrays and initiate sensors
# for x in range(1,16+1):
#         errorCode,sensor_handle=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor'+str(x),sim.simx_opmode_oneshot_wait)
#         sensor_h.append(sensor_handle) #keep list of handles        
#         errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor_handle,sim.simx_opmode_streaming)                
#         sensor_val=np.append(sensor_val,np.linalg.norm(detectedPoint)) #get list of values
        

# # t = time.time()


# # while (time.time()-t)<60:
# #     #Loop Execution
# #     sensor_val=np.array([])    
# #     for x in range(1,16+1):
# #         errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor_h[x-1],sim.simx_opmode_buffer)                
# #         sensor_val=np.append(sensor_val,np.linalg.norm(detectedPoint)) #get list of values

    
# #     #controller specific
# #     sensor_sq=sensor_val[0:8]*sensor_val[0:8] #square the values of front-facing sensors 1-8
        
# #     min_ind=np.where(sensor_sq==np.min(sensor_sq))
# #     min_ind=min_ind[0][0]
    
# #     if sensor_sq[min_ind]<0.2:
# #         steer=-1/sensor_loc[min_ind]
# #     else:
# #         steer=0
            
    
# #     v=1	#forward velocity
# #     kp=0.5	#steering gain
# #     vl=v+kp*steer
# #     vr=v-kp*steer
# #     print ("V_l =",vl)
# #     print ("V_r =",vr)

# #     errorCode=sim.simxSetJointTargetVelocity(clientID,left_motor_handle,vl, sim.simx_opmode_streaming)
# #     errorCode=sim.simxSetJointTargetVelocity(clientID,right_motor_handle,vr, sim.simx_opmode_streaming)


# #     time.sleep(0.2) #loop executes once every 0.2 seconds (= 5 Hz)

# #Post ALlocation
# errorCode=sim.simxSetJointTargetVelocity(clientID,left_motor_handle,0, sim.simx_opmode_streaming)
# errorCode=sim.simxSetJointTargetVelocity(clientID,right_motor_handle,0, sim.simx_opmode_streaming)

# res,dummyHandle = sim.simxCreateDummy(clientID, 0.1,None, sim.simx_opmode_blocking)
# sim.simxSetObjectOrientation(clientID, dummyHandle, -1, [0,0,0], sim.simx_opmode_blocking)
# res, cylinderHandle = sim.simxCreateCylinder(clientID, 0.5, 1, sim.simx_opmode_blocking)
# sim.simxSetObjectParent(clientID, dummyHandle, cylinderHandle, True, sim.simx_opmode_blocking)
# sim.simxSetObjectPosition(clientID, cylinderHandle, -1, [1,1,1], sim.simx_opmode_blocking)






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

