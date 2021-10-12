""" Python interface to the C++ Integer class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val, n):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]
		self.obj = lib.Integer_new(val)
		self.obj2 = lib.Integer_new(n)

	def get(self):
		return lib.Integer_get(self.obj)

	def fib_py(self, n):
		if n <= 1:
			return n
		else:
			return(self.fib_py(self, n-1) + self.fib_py(self, -2))

	def fib(self, n):
		return lib.Integer_fib(self.obj2, n)

	def set(self, val):
		lib.Integer_set(self.obj, val)
        
	def __del__(self):
		return lib.Integer_delete(self.obj)