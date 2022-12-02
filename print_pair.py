def print_pair(array):
    """ 
    - This function  print the pair of array
    this elements.
    - Argument : 
        - array : list 

    - Time Complexity : O(n2)
    """
    for i in array:
        for j in array:
            print(f"{i},{j}",end = " ")
        print("\n")
   

if __name__ == "__main__":
    """ 
    - This is main mfunction execution starts from here
    """
    array = [i for i in range(4)]
    print_pair(array)


