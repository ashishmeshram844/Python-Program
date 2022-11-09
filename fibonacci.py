""" WRITE A PROGRAM TO FIND FIBONACCI SERIES  """
import sys
sys.setrecursionlimit(50000)

def find_fibonacci(rng,lst=[0,1]):
    """ 
    This function find the fibonacci series upto a given number
    - Arguments : 
        - rng : int
        - lst : array
    """
    if len(lst) == rng:
        return lst[:rng]
    else:
        lst.append(lst[-1] + lst[-2])
        return find_fibonacci(rng,lst)


res = find_fibonacci(10000)
print(res)




from functools import lru_cache

@lru_cache(maxsize=50000)
def fibinacci(n = 10):
    """ 
    This function find fibonacci number of a a given number
    - Also User memoisation
    
    """
    if n in [0,1]:
        return n
    else:
        return fibinacci(n-1) + fibinacci(n-2)
        
print(fibinacci(40000))




