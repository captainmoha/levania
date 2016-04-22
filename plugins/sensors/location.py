from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.properties import StringProperty
from kivy.clock import Clock, mainthread
from kivy.uix.widget import Widget

class Location(App):

    gps_location = StringProperty("location not found")
    gps_status = StringProperty('Click Start to get GPS location ')
    gps_args = dict()

    def __init__(self):
        self.gps = gps
        try:
            self.gps.configure(on_location=self.on_location,
                               on_status=self.on_status)
            self.gps.start()
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])
        self.args = kwargs
        print self.args

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)
