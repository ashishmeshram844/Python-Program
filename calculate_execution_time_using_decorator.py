import time
def check_execution_time(function):
	""" 
	This is a decorator which calculate the function execution time
	"""
	def wrapper(*args, **kwargs):
		start = time.time()
		res = function(*args, **kwargs)
		end = time.time()
		print("TOTAL  : ",end-start)
		return res
	return wrapper

@check_execution_time
def abc():
	res = 1
	for i in range(1,100000):
		res = res*i 
abc()
