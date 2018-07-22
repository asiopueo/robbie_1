####################################################################
#
#   Node which requests commands and publishes on a twist topic
#
####################################################################

import cmd, sys
import math

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist



# Helper function
def parse(arg):
    #print (tuple(map(float, arg.split())))
    return tuple(map(float, arg.split()))


# ROS backend
class Publisher():
    def __init__(self):
        rospy.init_node('robbie_console', anonymous=False)
        self.publisher = rospy.Publisher('command', String, queue_size=10)

        # Default values:
        self.motorRPM = 80
        self.tireDiameter = 5. # circumference of tire: 2*PI*tireRadius or PI*diameter
        self.tireCirc = math.pi * self.tireDiameter

    def forward(self, length):
        print("Move forward by %3.1f cm." % length[0])
        rounds = length[0] / self.tireCirc
        time = rounds / self.motorRPM
        #return time, motorRPM
        self.publisher.publish('AfD')

    def backward(self, length):
        print("Move backward by %3.1f cm." % length[0])
        #rounds = length / tireCirc
        #time = rounds / motorRPM 
        #return time, motorRPM

    def left(self, deg):
        print("Turn left")
        pass

    def right(self, deg):
        print("Turn right")
        pass

    def quit(self):
        print('Shutting down node \'robbie_console\'...')
        rospy.signal_shutdown('Manual shutdown of node via Robbie\'s Shell.')
        #raise SystemExit()




# Frontend
class Shell(cmd.Cmd):
    def __init__(self):
        super(Shell, self).__init__()
        self.prompt = '(robbie) $ '
        self.intro = 'Welcome to Robbie\'s Shell. Enter \'help\' or \'?\' to list commands.\n'
        self.file = None # Later for waypoint files...
        self.pub = Publisher()

    # Basic commands:
    def do_forward(self, arg):
        'Move forward by the specified distance [cm]: FORWARD 10'
        #forward(*parse(arg))
        self.pub.forward(parse(arg))

    def do_backward(self, arg):
        'Move backward by the specified distance [cm]: BACKWARD 10'
        self.pub.backward(parse(arg))

    def do_left(self, arg):
        'Turn left by the specified angle [degree]: LEFT 45'
        self.pub.left(parse(arg))

    def do_right(self, arg):
        'Turn right by the specified angle [degree]: RIGHT 45'
        self.pub.right(parse(arg))

    def do_quit(self, arg):
        'Quit shell and shutdown node.'
        self.pub.quit()
        raise SystemExit()




if __name__=='__main__':
    Shell().cmdloop()




