from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import flickr_api
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.layout import Layout

class Gallery(BoxLayout):
	def __init__(self, **kwargs):
		self.albums = flickr_api.getAlbums()
		self.idx = 0
		Clock.schedule_interval(self.addImage, 1)
		self.ids['gl'].bind(minimum_height=self.ids['gl'].setter('height'))
		
	def clear(self, *args):
		self.ids.gl.clear_widgets()
	def addImage(self, *args):
		if self.idx < 15:
			from random import randint
			img = flickr_api.getRandomPic(album = self.albums[randint(0, len(self.albums)-1)]['id'])
			self.ids.gl.add_widget(AsyncImage(source = img, size_hint_y=None, allow_stretch = True, size = [size/3 for size in self.size]))
			self.idx+=1
			print "image added"
		else:
			return False
