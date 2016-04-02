"""
Represent various videogame controllers

TODO: Various play schemes/configs
XXX: UNTESTED
"""

import re

def setup_controls(joystick):
	"""
	Joystick wrapper.
	"""
	if re.search('playstation', joystick.get_name(), re.I):
		return Ps3Controller(joystick)

	elif re.search('X-box', joystick.get_name(), re.I):
		return XboxController(joystick)

	elif re.search('Saitek', joystick.get_name(), re.I):
		return MySaitekController(joystick)
	
	elif re.search('Thrustmaster dual analog 3.2', joystick.get_name(), re.I):
		return MyThrustController(joystick)
		
	elif re.search('2n1 USB', joystick.get_name(), re.I):
		return CSLController(joystick)

	return Controller(joystick)

class Controller(object):

	def __init__(self, joystick):
		"""Pass a PyGame joystick instance."""
		self.js = joystick

	def getLeftHori(self):
		return self.js.get_axis(2)

	def getLeftVert(self):
		return self.js.get_axis(3)

	def getRightHori(self):
		return self.js.get_axis(0)

	def getRightVert(self):
		return self.js.get_axis(1)

	def getLeftTrigger(self):
		return self.js.get_button(9)

	def getRightTrigger(self):
		return self.js.get_button(2)

class XboxController(Controller):

	def __init__(self, joystick):
		super(XboxController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(3)

	def getRightVert(self):
		return self.js.get_axis(4)

	def getLeftTrigger(self):
		return self.js.get_axis(2)

	def getRightTrigger(self):
		return self.js.get_axis(5)

class Ps3Controller(Controller):

	def __init__(self, joystick):
		super(Ps3Controller, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(2)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		# TODO: Verify
		return self.js.get_button(16)

	def getRightTrigger(self):
		# TODO: Verify
		return self.js.get_button(14)

class MySaitekController(Controller):

	def __init__(self, joystick):
		super(MySaitekController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(3)

	def getRightVert(self):
		return self.js.get_axis(2)

	def getLeftTrigger(self):
		return self.js.get_button(6)

	def getRightTrigger(self):
		return self.js.get_button(7)

class MyThrustController(Controller):

	def __init__(self, joystick):
		super(MyThrustController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(2)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		return self.js.get_button(5)

	def getRightTrigger(self):
		return self.js.get_button(7)


class CSLController(Controller):

	def __init__(self, joystick):
		super(CSLController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(2)

	def getLeftVert(self):
		return self.js.get_axis(3)

	def getRightHori(self):
		return self.js.get_axis(0)

	def getRightVert(self):
		return self.js.get_axis(1)

	def getLeftTrigger(self):
		return self.js.get_button(9)

	def getRightTrigger(self):
		return self.js.get_button(2)

