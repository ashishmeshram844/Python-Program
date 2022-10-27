""" REMOVE DUPLICATES FROM LIST AND SORT IN ASCENDING AND 
    DESCENDING ORDER WITHOUT USING INBUILT FUNCTIONS """

def input_list():
    """ 
    This function takes size of list and input the values 
    as size is inputed
    - returns -> list
    """
    size = int(input("Enter size of list : "))
    return list(int(input()) for i in range(size))
    
def get_unique_list(lst):
    """ 
    This function  return list of ubique elements
    - returns -> list
    """
    return list(set(lst))
    
def sort_list_in_ascending(lst):
    """ 
    This function sort the list in ascending order
    - Arguments : 
        - lst -> list of elements which we want to sort
    - returns:
        - lst -> sorted list
    """
    for i in range(len(lst)):
        def swap_element_in_list(j):
             if lst[i] < lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
        x = map(swap_element_in_list,range(len(lst)))
    return lst
  
def sort_list_in_descending(lst):
    """ 
    This function sort the list in descending order
    - Arguments : 
        - lst -> list of elements which we want to sort
    - returns:
        - lst -> sorted list
    """
    return lst[::-1]

def main():
    """ 
    Execution of program starts from here
    """
    lst = input_list()
    print(sort_list_in_ascending(get_unique_list(lst)))
    print(sort_list_in_descending(sort_list_in_ascending(get_unique_list(lst))))

if __name__ == "__main__":
    main()
 
