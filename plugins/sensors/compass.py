from jnius import autoclass
from accelero import Accelero
from magnetometer import Magnetometer
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.app import App

SensorManager = autoclass('android.hardware.SensorManager')

class Compass(Widget):

	orientation = [0.0, 0.0, 0.0]
	
	def __init__(self):
		super(Compass, self).__init__()
		self.acc = Accelero()
		self.mag = Magnetometer()
		Clock.schedule_interval(self.getOrientation, 1 / 10.)

	def getOrientation(self, *args):
		R = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		I = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
		success = False
		try:
			mGravity = [float(x) for x in self.acc.output]
			mGeomagnetic = [float(x) for x in self.mag.output]
			success = SensorManager.getRotationMatrix(R, I, mGravity, mGeomagnetic)
		except Exception, error:
			print str(error)
			self.orientation = [0.0, 0.0, 0.0]

		if (success):
			import math
			
			SensorManager.getOrientation(R, self.orientation)
			print "orientation : "
			self.orientation = [x*180/math.pi for x in self.orientation]
			self.orientation[0]=abs(self.orientation[0])
			print self.orientation
		else:
			print "failed"
