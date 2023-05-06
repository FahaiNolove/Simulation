try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import sys

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
print ("client id:",clientID)   #checking message, delete later

if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Connection failed')
    sys.exit('Could not connect!')

#left motor handle
errorCode,left_motor_handle = sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',sim.simx_opmode_oneshot_wait)
print ("errorCode:",errorCode)  #checking message, delete later
print("left moter handle:",left_motor_handle)   #checking message, delete later

#right motor handle
#errorCode,right_motor_handle = sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',sim.simx_opmode_oneshot_wait)
#print ("errorCode:",errorCode)  #checking message, delete later
#print("left moter handle:",right_motor_handle)  #checking message, delete later

#set robot joint velocity
#errorCode = sim.simxSetJointTargetVelocity(clientID,left_motor_handle,0.2,sim.simx_opmode_streaming)    #set the target velovity to 0.2
#errorCode = sim.simxSetJointTargetVelocity(clientID,right_motor_handle,0.2,sim.simx_opmode_streaming)    #set the target velovity to 0.2

#set sensor 1
errorCode,sensor1 = sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',sim.simx_opmode_oneshot_wait)
print ("errorCode:",errorCode)  #checking message, delete later
print("sensor 1:",sensor1)   #checking message, delete later

#errorCode, detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector = sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_streaming)
#errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_streaming)        
errorCode, detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector = sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_buffer)
print ("errorCode:",errorCode)  #checking message, delete later
print("detectionState:",detectionState)   #checking message, delete later
print("detectedPoint",detectedPoint)   #checking message, delete later
print ("detectedObjectHandle:",detectedObjectHandle)  #checking message, delete later
print("detectedSutfaceNormalVector:",detectedSurfaceNormalVector)   #checking message, delete later


