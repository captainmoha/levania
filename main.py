from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.androidtabs import *

class MyTab(BoxLayout, AndroidTabsBase):
	pass

class MoonTab(MyTab):

	pass

class ImagesTab(MyTab):
	pass

class StoriesTab(MyTab):
	pass


class LevaniaApp(App):
	def build(self):
		android_tabs = AndroidTabs()
		titles = ["something", "something"]

		tab = MoonTab(text="Find Luna")
		android_tabs.add_widget(tab)

		tab = ImagesTab(text = "Explore images")
		android_tabs.add_widget(tab)

		tab = StoriesTab(text = "Read Stories")
		android_tabs.add_widget(tab)
		for t in titles:
			tab = MyTab(text=t)
			android_tabs.add_widget(tab)
		return android_tabs


if __name__ == '__main__':
	LevaniaApp().run()