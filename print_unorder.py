
def print_unorder_pair(array):
    """ 
    - This function  print the unordered pair of array
    this elements.
    - Argument : 
        - array : list 
    - Time Complexity : O(nlogn)
    """
    for i in array:
        for j in range(i+1,len(array)):
            print(f"{i},{j}", end = " ")
        print("\n")

   
if __name__ == "__main__":
    """ 
    - This is main mfunction execution starts from here
    """
    array = [i for i in range(4)] 
    print_unorder_pair(array)

    
