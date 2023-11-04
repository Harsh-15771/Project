import kivy
import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('calculator.kv')

Window.size = (500,700)

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	def number(self,button):
		prior= self.ids.calc_input.text

		if prior == 'Error':
			prior=''

		if prior=='0':
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'

		else:
			self.ids.calc_input.text = f'{prior}{button}'

	def math_sign(self,sign):
		prior= self.ids.calc_input.text
		if prior[-1] in ['+','-','*','÷']:
			prior = prior[:-1]+sign
			self.ids.calc_input.text = f'{prior}'

		else:
			self.ids.calc_input.text = f'{prior}{sign}'

	def dot(self):
		prior= self.ids.calc_input.text
		for i in ['+','-','*','÷']:
			prior=' '.join(prior.split(i))

		num_list= prior.split()

		prior= self.ids.calc_input.text

		for i in ['+','-','*','÷']:
			if i in prior and '.' not in num_list[-1]:
				self.ids.calc_input.text = f'{prior}.'
		
		if '.' in prior:
			pass

		else:
			self.ids.calc_input.text = f'{prior}.'


	def cent(self):
		prior= self.ids.calc_input.text
		if prior.isnumeric():
			self.ids.calc_input.text = f'{prior}%'

		else:
			self.ids.calc_input.text = 'Error'


	def remove(self):
		prior= self.ids.calc_input.text
		prior = prior[:-1]
		self.ids.calc_input.text = f'{prior}'

	def sign_change(self):
		prior= self.ids.calc_input.text

		for i in range(len(prior)):
			if prior[-(i+1)] in ['+','-','*','÷']:
				prior=prior[:-i]+f'(-{prior[-i:]})'
				break

		else:
			prior=f'(-{prior})'

		self.ids.calc_input.text = f'{prior}'
		


	def equals(self):
		prior= self.ids.calc_input.text

		try:
			if prior[-1]=='%':
				self.ids.calc_input.text = str(int(prior[0:-1])/100)
			else:
				answer= eval(prior)
				answer = round(answer,2)
				self.ids.calc_input.text = str(answer)

		except:
			self.ids.calc_input.text = 'Error'


class Calculator(App):
	def build(self):
		self.icon = 'download.png'
		return MyLayout()

if __name__=='__main__':
	Calculator().run()