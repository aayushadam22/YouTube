import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from covid import Covid

class Window(GridLayout):
	covid = Covid()
	con=ObjectProperty(None)
	conf=ObjectProperty(None)
	act=ObjectProperty(None)
	rec=ObjectProperty(None)
	d=ObjectProperty(None)
	data={}
	def btn(self):
		if self.con.text=='' or self.con.text=='Enter a valid country.':
			self.con.text='Enter a valid country.'
		else:
			self.data=self.covid.get_status_by_country_name(self.con.text)
			self.conf.text=str(self.data['confirmed'])
			self.act.text=str(self.data['active'])
			self.rec.text=str(self.data['recovered'])
			self.d.text=str(self.data['deaths'])


class MyApp(App):
	def build(self):
		return Window()

MyApp().run()