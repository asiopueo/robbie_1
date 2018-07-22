####################################################################
#
#	Node which requests commands and publishes on a twist topic
#
####################################################################


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist



class Command:
	__init__(self):
		# command() being the callback function
		self.publisher = rospy.Publisher('command', String, queue_size=10)


	def command():
		r = rospy.Rate(10)
		while not rospy.is_shotdown():
			cmd = input('Please enter command:')
			print('You have entered the command {}'.format(cmd))
			self.publisher.publish(cmd)
			r.sleep()


# fixed rpm of motor
motorRPM = 80

# circumference of tire: 2*PI*tireRadius or PI*diameter
tireDiameter = 0.
tireCirc = PI * tireDiameter



def forward(length):
	rounds = length / tireCirc
	time = rounds / motorRPM
	return time, motorRPM


def backward(length):
	rounds = length / tireCirc
	time = rounds / motorRPM 
	return time, motorRPM

def left(deg):
	pass



def right(deg):
	pass

















if __name__=='__main__':
	try:
		cmd = Command()
	except rospy.ROSInterruptException:
		pass
