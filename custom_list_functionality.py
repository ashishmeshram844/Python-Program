import ctypes

class Mylist:
	def __init__(self):
		self.size = 1
		self.n = 0
		self.A = self.__create_array(self.size)

	def __len__(self):
		return self.n

	def append(self,num):
		# append data values in array 
		if self.n == self.size:
			self.__resize_array(self.size*2)
		self.A[self.n] = num
		self.n += 1

	def __str__(self):
		lst = ''
		for i in range(self.n):
			lst = lst + str(self.A[i]) + ','
		return '[' + lst + ']'

	def __resize_array(self,size):
	# resize array because array is full
		B = self.__create_array(size)
		self.size = size
		# copy content from A array to B Array
		for i in range(self.n):
			B[i] = self.A[i]
		self.A = B

	def __create_array(self,capacity):
		# this function creates new array with size capacity
		return (capacity*ctypes.py_object)()

L = Mylist()
L.append("Hello")
L.append("dfsdf")
L.append(55)
print(L)
