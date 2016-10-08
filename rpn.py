#!/usr/bin/env python3
from tkinter import *
import operator
import readline
operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,

}
def frame(root, side):
	
	w = Frame(root)
	w.pack(side = side, expand = YES, fill = BOTH)
	return w
def button(root, side, text, command = None):
	w =  Button(root, text = text, command = command)
	w.pack(side = side, expand = YES, fill = BOTH)
	return w
class Calculator(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack(expand = YES, fill = BOTH)
		self.master.title('Calculater')
		display = StringVar()
		Entry(self, relief = SUNKEN, 
			textvariable = display).pack(side = TOP, expand = YES, fill = BOTH)
		
		for key in ('123', '456', '789', ' 0.'):
			keyF = frame(self, TOP)
			for char in key:
				button(keyF, LEFT, char, lambda w = display, c = char:w.set(w.get()+c))
		
		opsF=frame(self,TOP)
		
		for char in '+-*/=':
			if char == '=':
				btn = button(opsF, LEFT, char)

				btn.bind('<ButtonRelease - 1>', lambda e, s=self, w = display:calculate_helper(w))
			else:
				btn = button(opsF, LEFT, char, lambda w = display, s = '%s' %char:w.set(w.get()+s))
		
		clearF=frame(self,BOTTOM)
		button(clearF, LEFT, 'clear', lambda w= display:w.set(''))
	
def calculate_helper(myarg):
	myarg.set(calculate(myarg.get()))

def calculate(myarg1):
	stack = list()
	for token in myarg1.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = operators[token]
			result = function(arg1,arg2)
			stack.append(result)
		print(stack)
	if len(stack) !=1:
		raise TypeError
	return stack.pop()

def meaningless():
	print("This is meaningless")
	print("In order to test coveralls")

def main():
	while True:
		calculate(input("rpn calc> "))
if __name__ == '__main__': # Note that's "underscore underscore n a m e ..."
	#main()
	root=Tk();
	root.title("Calculator")
	Calculator().mainloop()