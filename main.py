from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class LevBox(BoxLayout):
	pass


class LevaniaApp(App):

	def build(self):
		return LevBox()

if __name__ == '__main__':
	LevaniaApp().run()