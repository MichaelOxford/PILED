import sys
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print('Error importing RPi.GPIO. Are we running on a Raspberry Pi?')
    sys.exit()
except RuntimeError:
    print("Can't run module. Do we need to run as sudo?")
    sys.exit()
class Raspberry_pi:
    """ Creates a raspberry Pi object to use with inputs and outputs """
    def __init__(self):
        self.GPIO = GPIO
        self.set_board_mode('BCM')
        self.set_warnings('TRUE')
        self.mode = self.display_mode()
        self.warnings = self.GPIO.setwarnings(False)
        self.rpi_info = self.GPIO.RPI_INFO
        self.rpi_revision = self.GPIO.RPI_INFO['P1_REVISION']
        self.gpio_version = self.GPIO.VERSION
    def display_mode(self):
        mode = self.GPIO.getmode()
        if mode == -1:
            print('GPIO Mode: None')
        elif mode == 10:
            print('GPIO Mode: Board')
        elif mode == 11:
            print('GPIO Mode: BCM')
        else:
            print('Error getting mode')
    def set_board_mode(self, numbering):
        if str.upper(numbering) == 'BCM':
            self.mode = self.GPIO.setmode(self.GPIO.BCM)
        elif str.upper(numbering) == 'BOARD':
            self.mode = self.GPIO.setmode(self.GPIO.BOARD)
    def set_warnings(self, state):
        if str.upper(state) == 'TRUE':
            self.GPIO.setwarnings(True)
        elif str.upper(state) == 'FALSE':
            self.GPIO.setwarnings(False)
    def cleanup(self):
        self.GPIO.cleanup()
    def print_pi_details(self):
        print('Board mode: ', self.mode)
        print('Board Information: ', self.rpi_info)
        print('Board revision: ', self.rpi_revision)
        print('GPIO version: ', self.gpio_version)
if __name__ == '__main__':
    pi = Raspberry_pi()
    pi.print_pi_details()
    pi.cleanup()
