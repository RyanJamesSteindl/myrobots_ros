#!/usr/bin/env python
# license removed for brevity
import sys, rospy, MyRobots, random, time
from std_msgs.msg import *

class MyRobotsData:
	def __init__(self):
		#setup parameters
		self.set_params()
		#Setup subscribers
		self.setup_subscribers()
		#send data to server
		self.send_data()

	def set_params(self):
		#Inital parameters for the node
		#KEY
		self.keys = [rospy.get_param('/myrobots/key', '0000000000000000')]
		#setup myrobots robot object		
		self.robots = [MyRobots.Robot(k) for k in self.keys]
		## Set the location
		# time period
		self.period = 15
		
		# Initial parameters for myrobots fields
		self.field_1_msg = 10
		self.field_2_msg = 20
		self.field_3_msg = 30
		self.field_4_msg = 40
		self.field_5_msg = 50
		self.field_6_msg = 60
		self.field_7_msg = 70
		self.field_8_msg = 80
		
		self.status_msg = 'Initial'
		self.location_msg = 'Home sweet home'		

		self.dec_lat = -27.4709
		self.dec_long = 153.0235
		self.dec_elev = 33.05
	

	def setup_subscribers(self):
		# setup field topics for subscribers
		#FIELD 1
		self.field_1_topic = rospy.get_param('/myrobots/field_1_topic','/field1')
		self.field_1_data_type = rospy.get_param('/myrobots/field_1_data_type','Int16')
		#FIELD 2
		self.field_2_topic = rospy.get_param('/myrobots/field_2_topic','/field2')
		self.field_2_data_type = rospy.get_param('/myrobots/field_2_data_type','Int16')
		#FIELD 3
		self.field_3_topic = rospy.get_param('/myrobots/field_3_topic','/field3')
		self.field_3_data_type = rospy.get_param('/myrobots/field_3_data_type','Int16')
		#FIELD 4
		self.field_4_topic = rospy.get_param('/myrobots/field_4_topic','/field4')
		self.field_4_data_type = rospy.get_param('/myrobots/field_4_data_type','Int16')
		#FIELD 5
		self.field_5_topic = rospy.get_param('/myrobots/field_5_topic','/field5')
		self.field_5_data_type = rospy.get_param('/myrobots/field_5_data_type','Int16')
		#FIELD 6
		self.field_6_topic = rospy.get_param('/myrobots/field_6_topic','/field6')
		self.field_6_data_type = rospy.get_param('/myrobots/field_6_data_type','Int16')		
		#FIELD 7
		self.field_7_topic = rospy.get_param('/myrobots/field_7_topic','/field7')
		self.field_7_data_type = rospy.get_param('/myrobots/field_7_data_type','Int16')
		#FIELD 7
		self.field_8_topic = rospy.get_param('/myrobots/field_8_topic','/field8')
		self.field_8_data_type = rospy.get_param('/myrobots/field_8_data_type','Int16')
		#STATUS		
		self.status_topic = rospy.get_param('/myrobots/status_topic','/status')
		self.status_data_type = rospy.get_param('/myrobots/status_data_type','String')
		#LOCATION
		self.location_topic = rospy.get_param('/myrobots/location_topic','/location_topic')
		self.location_data_type = rospy.get_param('/myrobots/location_data_type','String')

		#LONG/LAT/ELEV
		#todo!

		#####################
		#Setup Subscribers
		#####################
		#FIELD 1 
		rospy.Subscriber(self.field_1_topic, str_to_class(self.field_1_data_type), self.field_1_callback)
		#FIELD 2 
		rospy.Subscriber(self.field_2_topic, str_to_class(self.field_2_data_type), self.field_2_callback)
		#FIELD 3 
		rospy.Subscriber(self.field_3_topic, str_to_class(self.field_3_data_type), self.field_3_callback)
		#FIELD 4 
		rospy.Subscriber(self.field_4_topic, str_to_class(self.field_4_data_type), self.field_4_callback)
		#FIELD 5 
		rospy.Subscriber(self.field_5_topic, str_to_class(self.field_5_data_type), self.field_5_callback)
		#FIELD 6 
		rospy.Subscriber(self.field_6_topic, str_to_class(self.field_6_data_type), self.field_6_callback)
		#FIELD 7 
		rospy.Subscriber(self.field_7_topic, str_to_class(self.field_7_data_type), self.field_7_callback)
		#FIELD 8 
		rospy.Subscriber(self.field_8_topic, str_to_class(self.field_8_data_type), self.field_8_callback)
		#STATUS
		rospy.Subscriber(self.status_topic, str_to_class(self.status_data_type), self.status_callback)
		#LOCATION
		rospy.Subscriber(self.location_topic, str_to_class(self.location_data_type), self.location_callback)
	
	def field_1_callback(self, message):
		self.field_1_msg = message.data

	def field_2_callback(self, message):
		self.field_2_msg = message.data

	def field_3_callback(self, message):
		self.field_3_msg = message.data

	def field_4_callback(self, message):
		self.field_4_msg = message.data

	def field_5_callback(self, message):
		self.field_5_msg = message.data

	def field_6_callback(self, message):
		self.field_6_msg = message.data

	def field_7_callback(self, message):
		self.field_7_msg = message.data

	def field_8_callback(self, message):
		self.field_8_msg = message.data

	def status_callback(self, message):
		self.status_msg = message.data

	def location_callback(self, message):
		self.location_msg = message.data	

	def send_data(self):
		while not rospy.is_shutdown():
			for r in self.robots:
				## Fill parameters with random data
				r.parameters['field1'] = self.field_1_msg
				r.parameters['field2'] = self.field_2_msg
				r.parameters['field3'] = self.field_3_msg
				r.parameters['field4'] = self.field_4_msg
				r.parameters['field5'] = self.field_5_msg
				r.parameters['field6'] = self.field_6_msg
				r.parameters['field7'] = self.field_7_msg
				r.parameters['field8'] = self.field_8_msg
				r.parameters['status'] = self.status_msg
				r.parameters['location'] = self.location_msg				
				r.parameters['lat'] = self.dec_lat
				r.parameters['long'] = self.dec_long
				r.parameters['elevation'] = self.dec_elev	
				
				## Print the robot key for debugging purposes.
				print r.parameters['key']
				## send robot data to MyRobots.com
				r.write()
    			time.sleep(self.period)

def str_to_class(str):
	return getattr(sys.modules[__name__],str)


	
if __name__ == '__main__':
	try:
		rospy.init_node('myrobots_ros', anonymous=True)
		MyRobotsData()		
	except rospy.ROSInterruptException:
		pass

