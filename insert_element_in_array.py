""" Insert element in array on given position """

class Elementinsertion:
    def __init__(self):
        pass
    
    def inputArray(self):
        """ 
        This function takes the array size and array inputs from  user
        """
        size_of_array = int(input("Enter the size of Array : "))
        print("Input Array values with space seperated : ",end = " ")
        array = list(map(int,input().split()))
        if len(array) > size_of_array:
            print(f"We take only starting {size_of_array} element from your input")
        elif len(array) < size_of_array:
            print(f"You provide less inputs we require {size_of_array} but you gave {len(array)} so we addedd rest of values as None")
            for i in range(len(array),size_of_array):
                array.append(None)
            
            
        self.array =  array[:size_of_array]
        return
    
    def inputInsertionData(self):
        """
        This function take the inputs which we want to insert in inputed array
        """
        self.position = int(input("Enter position where you want to add element : "))
        self.value = int(input(f"Enter a value which you want to place in {self.position} : "))
        return
    
    def InsertValueAtPosition(self):
        """
        This function insert the value to user inputed position 
        """
        self.array.append(-1)
        for i in range(len(self.array)-1,self.position-1,-1):
            self.array[i] = self.array[i-1]
        self.array[self.position-1] = self.value
    
    def printArray(self):
        """ This function print the array values """
        print(self.array)
    

if __name__ == "__main__":
    obj = Elementinsertion()
    obj.inputArray()
    obj.printArray()
    obj.inputInsertionData()
    obj.InsertValueAtPosition()
    obj.printArray()
    
