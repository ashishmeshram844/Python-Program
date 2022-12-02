""" WRITE A PROGRAM TO CHECK GIVEN ARRAY IS SORTED OR NOT"""

def check_sorted(lst):
    """ 
    This function checks the list is sorted or not
    - Arguments : 
        - lst : array (inputed array)
    """
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
            break
    else:
        return True

def main():
    lst = [1,2,3,4,5,6,7,8,9,10]
    if check_sorted(lst):
        print("sorted")
    else:
        print("Not sorted")

if __name__ == "__main__":
    """ 
    Execution Starts from Here
    """
    main()
