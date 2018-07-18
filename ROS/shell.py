import cmd
# also import the robot's-functionality library!
# [...]

# Helper function
def parse():
    pass


class Shell(cmd.Cmd):
    intro = 'Welcome to Robbie\'s shell. Type \'help\' or \'?\' to list commands.\n'
    prompt = '(robbie)'
    file = None # Meaning of this?

    # Basic commands:

    def do_forward(self, arg):
        'Move forward by the specified distance [cm]: FORWARD 10'
        forward(*parse(arg))

    def do_backward(self, arg):
        'Move backward by the specified distance [cm]: BACKWARD 10'
        backward(*parse(args))

    def do_left(self, arg):
        'Turn left by the specified angle [degree]: LEFT 45'
        left(*parse(arg))

    def do_right(self, arg):
        'Turn right by the specified angle [degree]: RIGHT 45'
        right(*parse(arg))






if __name__=='__main__':
    Shell().cmdloop()
