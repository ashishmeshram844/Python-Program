"""
PROGRAMME TO CALULATE SUM OF ALL ELEMENTS IN A GIVEN LIST
"""

def get_input():
    """
    This function takes the inputs from user
    - Used vars : 
        - n : number of elements in list
        - lst : all elements are stored
    - return :
        - lst : list containg all user inputed values
    """
    try:
        n = int(input("Enter a number which you want to add in list : "))
        lst = [int(input(f"Enter number {i+1} : ")) for i in range(n)]
        return lst
    except Exception as e:
        print(e)

def sum_of_list(lst : list = None):
    """
    This function find the sum of all elements available in list
    - Args :
        - lst : list object which contain all elements
    """
    if isinstance(lst,list):
        if len(lst) == 1:
            return lst[0]
        else:
            return lst[0] + sum_of_list(lst[1:])
    else:
        return "List is not provided"

if __name__ == "__main__":
    lst = get_input()
    if lst:
        print(sum_of_list(lst))

