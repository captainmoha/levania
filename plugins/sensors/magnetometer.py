import kivy
from jnius import autoclass
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.animation import Animation

Hardware = autoclass('org.renpy.android.Hardware')

class Magnetometer:
	output = (0,0,0)
	def __init__(self):
		Hardware.magneticFieldSensorEnable(True)
		Clock.schedule_interval(self.update_magnetometer, 1 / 10.)
	
	def update_magnetometer(self, *args):
		self.output = Hardware.magneticFieldSensorReading()
		print self.output
		
