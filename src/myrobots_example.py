#!/usr/bin/env python
# license removed for brevity
import rospy, MyRobots, random, time
from std_msgs.msg import *


def talker():
	#set up publishers and subscribers 
	
	field_1_pub = rospy.Publisher('field1', Int16, queue_size=1)
	field_2_pub = rospy.Publisher('field2', Int16, queue_size=1) 

	status_pub = rospy.Publisher('status', String, queue_size=1)
 	
	#Initilize ros node
	rospy.init_node('myrobots_random_pub', anonymous=True)
	#Publish rate Needs to be peramiterised
	rate = rospy.Rate(1)
	#setup Status mesages 
	field_1_msg = 1	
	field_1_msg = 1	
	status_msg = ['Happy',
              	'Sad',
              	'Cleaning',
              	'Charging',
              	'Stuck',
              	'Confused',
              	"Here I am, brain the size of a planet, \
and they ask me to take you to the bridge. \
Call that job satisfaction, 'cause I don't.",
              	"I think you ought to know I'm feeling very depressed.",
              	"I've calculated your chance of survival, \
but I don't think you'll like it. ",
              	"Hasta la vista baby.",
              	"EXTREMINATE!",
              	"DELETE!",
              	"MyRobots.com is Live!! Finaly robots can get a social life",
              	"Come with me if you want to live"]

	while not rospy.is_shutdown():    
		
		field_1_msg = random.randint(10, 40)
		field_2_msg = random.randint(100, 400)
		status_str = random.choice(status_msg)
		#rospy.loginfo(status_str)

		#publish topics
		field_1_pub.publish(field_1_msg)
		field_2_pub.publish(field_2_msg)
		
		status_pub.publish(status_str)
		
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
