import rospy
from std_msgs.msg import String
import serial

SERIAL_PORT = '/dev/ttyACM0'


class controller:
	def __init__(self):
		rospy.init_node('motor_controller', anonymous=True)
		rospy.Subscriper()
		# Lower boud rate to publish motor commands might be appropriate
		self.ser = serial.Serial('/dev/ttyACM0', 115200)
		self.

	def motor_command():
		left = pwm()
		right = pwm()
		command = '{},{}'.format(left, right) 
		self.ser.write(command)

	def publisher():
		pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=3)
		pub.publish(std_msgs.msg.String('foo'))
	





if __name__=='__main__':
	print("Starting Command Publisher node")
	try:	
		c = controller()
	except rospy.ROSInterruptException:
		pass


