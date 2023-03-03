""" 
LINEAR SEARCH 
"""

def array_input(n):
    """ This function takes the array input values """
    return [int(input(f"Enter {i+1} value : ")) for i in range(n)]

def search_in_array(a,val):
    """ This function search the value in user inputed array """
    if val in a:
        return f"{val} is present in {a} on index {a.index(val)}"
    else:
        return f"{val} is not present in {a}"
    
if __name__ == "__main__":
    test_cases_count = int(input("Enter How many test cases are going to give : "))
    while test_cases_count:
        n = int(input("Enter How many items you want to add in array : ")) 
        a = array_input(n)
        search_val = int(input("Enter a search value : "))
        result = search_in_array(a,search_val)
        print(result)
        test_cases_count-=1

