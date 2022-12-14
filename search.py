""" WRITE A PROGRAM FOR SEARCHING """

def input_list():
    """ 
    This function takes size of list and input the values 
    as size is inputed
    - returns -> list
    """
    size = int(input("Enter size of list : "))
    lst = list(int(input()) for i in range(size))
    search_val = int(input("Enter value to search in Inputed List : "))
    return lst,search_val
    
def get_unique_ele_list(lst):
    """ 
    This function  return list of ubique elements
    - returns -> list
    """
    return list(set(lst))

def search_value(search_val,lst):
    """ 
    This function search the inputed element is present in list or not
    """
    return True if search_val in lst else False

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

def binary_search(search_val,lst):
    """ 
    - This function  devide list into two part and check 
      is available search value is present in list or not 
    - Arguments: 
        - search_val : its a value we want to search in list
        - lst : is a list where we want to search items are present or not
    - returns: 
        - boolean (True/False)
    """
    low = 0
    high = len(lst) - 1
    while (low <= high):
        mid = ((low + high)//2)
        if sorted_lst[mid] == search_val:
            return True
            break
        elif search_val > sorted_lst[mid]:
            low = mid + 1
        elif search_val < sorted_lst[mid]:
            high = mid - 1
    return False
        

def main():
    lst,search_val = input_list()
    non_duplicate_items_list = get_unique_ele_list(lst)
    sort_list_in_ascending(non_duplicate_items_list)
    print("Available") if search_value(search_val,non_duplicate_items_list) else print("Not Available")
    print("Available") if binary_search(search_val,non_duplicate_items_list) else print("Not Available")

if __name__ == "__main__":
    """ 
    Execution starts from here
    """
    main()
