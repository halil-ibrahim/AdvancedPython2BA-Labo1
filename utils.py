# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt, sin ,cos,pi
from scipy.integrate import quad

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n<0:
		raise ValueError("must be >=0")
	if n ==0:
		return 1
	facto = 1
	for i in range(1,n+1):
		facto=facto*i
	return facto
	pass

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	racine = ()
	delta=(b*b)-4*a*c
	if delta>0:
		racine=((((-b)+sqrt(delta))/(2*a)),(((-b)-sqrt(delta))/(2*a)))
		return racine
	if delta==0:
		racine=((-b)/(2*a))
		return racine
	if delta<0:
		raise ValueError("delta est négatif")
		return racine 


def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""

	def f(x):
		return eval(function)

	I = quad(f,lower,upper)
	return I[0]
	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 3, 2))
	print(integrate('x ** 2 - 1', -1, 1))
