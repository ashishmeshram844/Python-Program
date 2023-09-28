""" Find Sum of Numbers  within given range """
import sys
sys.setrecursionlimit(50000)
from functools import lru_cache

class CalculateSum:
    """ This class contain all operations for calculating the sum of number 
        betweeen the given range
    """
    def __init__(self):
        pass
    def takeInputs(self):
        """ This function takes the starting and ending range values from user"""
        try:
            self.start_val = int(input("Enter Starting : "))
            self.end_val = int(input("Enter End : "))
            return True
        except ValueError: 
            print("Integer Required ... ")
            return False
        else:
            return False
    
    def printInputs(self):
        """ This function simply shows text that our calculation is in process """
        print(f"calculating sum from {self.start_val } to {self.end_val} ...")
    
    @lru_cache(maxsize=50000)
    def calculation(self,end_val):
        """ This function calculate the sum of given range recursively """
        if end_val < self.start_val:
            return 0
        else:
            return end_val + self.calculation(end_val -1)
       
       
if __name__ == "__main__":
    """ Main mehod Execution Starts from here """
    obj = CalculateSum()
    if obj.takeInputs():
        obj.printInputs()
        print("Answer is : ",obj.calculation(obj.end_val))
        
        
                
