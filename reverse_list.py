""" Reverse a list """

def reverse_list(lst):
    """
    - This function reverse the given list
    - Argument : 
        - lst : list
    - return :
        lst : reversed list
    - Time Complexity : log(n)
    """
    for i in range(len(lst)//2):
        other = len(lst)-i-1
        temp = lst[other]
        lst[other] = lst[i]
        lst[i] = temp  
    return lst
  
if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9]
    res = reverse_list(lst)
    print(res)


