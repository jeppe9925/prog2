#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

pyTime = []
cppTime = []

def main():
	I = Integer(30)  # skapar ett klassobject integer med int = 30
	nlst = range(30,45) 
	print(nlst)  # range från 30 till 45
	for i in nlst: # för alla värden
		I.set(i) # ansätt nytt värde för Int i klassobjektet I

		start = pc()  #Cpp tidtagning för fib. tider före, efter sedan skillnad.
		print(I.fib()) 
		end = pc()
		print(round(end-start,2))
		cppTime.append(end - start)

		start = pc() #Py Samma här
		print(fib_py(i))
		end = pc()
		print(round(end-start,2))
		pyTime.append(end - start)

	I.set(47) 
	start = pc()
	print("Test 47 cpp: ", I.fib())
	end = pc()
	print("Time for n = 47 with cpp: ", end - start) 

	plt.plot(nlst, cppTime, 'b.', nlst, pyTime, 'r.')
	plt.xlabel('Iterations (n)')
	plt.ylabel("Time for fibonacci (s)")
	plt.savefig('fib_py_cpp.png')



def fib_py(n): #fib python
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

if __name__ == '__main__':
	main()
