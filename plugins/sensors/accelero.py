from plyer import accelerometer #object to read the accelerometer
from kivy.clock import Clock #clock to schedule a method
from kivy.uix.widget import Widget
class Accelero(Widget):
	output = (0,0,0)

	def __init__(self):
		accelerometer.enable() #enable the accelerometer
		Clock.schedule_interval(self.update, 1.0/24)

	def update(self, dt):
		self.output = (accelerometer.acceleration[0], accelerometer.acceleration[1], accelerometer.acceleration[2])