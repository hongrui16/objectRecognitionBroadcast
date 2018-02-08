#!/usr/bin/env python
# -*- coding: utf-8 -*-  


import rospy
from std_msgs.msg import String
from translate_bd import Baidu_Translation


class RosTranslateFlow():
	def __init__(self):
		self.sub = rospy.Subscriber('enchatter', String, self.callback,queue_size=1)
		self.pub = rospy.Publisher('xfwords', String, queue_size=1)

	def callback(self, data):
#		print data.data
		Trans = Baidu_Translation()
		result = Trans.StartTrans(data.data)
		print result  
		self.pub.publish(result)
	def main(self):
		rospy.spin()

if __name__ == '__main__':
    rospy.init_node('TranlateNode', anonymous=True)
    trannode = RosTranslateFlow()
    trannode.main()



