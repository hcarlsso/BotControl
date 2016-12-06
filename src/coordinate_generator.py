#!/usr/bin/env python
'''
This source will act as best effort support & does not follow best
coding practices.

This code is intended to test the interface between planner and low-level turtle bot controller
When you are running the code, it will ask about coordinate to drive
this part will be provided within use case by the planner
Then this coordinate will be sent to right topic to inform the turtle boat to drive to that

Copyright @KTH
'''

#Import Python Packages, ROS messages used.
#You might not need all of below package -
import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PointStamped
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
import time
import numpy as np



# Array that keeps information about goals and completed goals
goals = []

def start():

    global goal_pub, poseArray_pub

    #Initialize the ROS Node for this functionality
    rospy.init_node('Test_coordinate')

    #Initialize publisher to publish PoseArray with list of goals to tb_path_publisher
    # The tb_path_publisher listen to topic "/list_of_goals"
    poseArray_pub = rospy.Publisher("/list_of_goals", PoseArray, queue_size = 1)

    print "Please enter the coordinate"
    x = float (input("x: "))
    y = float (input("y: "))


    global goals

    #Update the list of goals by appending the Currently received point.
    goals.append([x,y])

    i = 0
    #Create an object to new pose array
    newPoseArray = PoseArray()
    #assign frame of these pose objects as map
    newPoseArray.header.frame_id = "map"
    #Boundary Checks
    if(len(goals)!=0):
        #Update all the goals to the Pose array by appending new element to the
        #pose array
        for goal in goals:
            newPoseArray.poses.append(Pose())
            newPoseArray.poses[i].position.x = goal[0]
            newPoseArray.poses[i].position.y = goal[1]
            i = i+1
        #Publish the new list to the tb_path_publisher to move the robot.
        poseArray_pub.publish(newPoseArray)
	print newPoseArray

#TO DO  - we are not receiving the feedback for accomplished goal
# the main objective of this code is to test the functionality
# later you might want to get a feedback and remove the completed goal from the list


if __name__ == '__main__':
    try:
        start()
    except rospy.ROSInterruptException:
        pass
