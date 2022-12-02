def find_sum_and_product(array):
    """ 
    - This function  list of numbers and find the sum and product of all
    this elements.
    - Argument : 
        - array : list 
    returns : 
        - sum : int (sum of elements presenet in array)
        - product : int (product of elements present in array)
    """
    sum,product = 0,1
    for num in array:
        sum += num
        product *= num
    return sum,product

if __name__ == "__main__":
    """ 
    - This is main mfunction execution starts from here
    - generate array between range 1 to 12 with diffrence of 3
    """
    array = [i for i in range(1,12,3)]
    sum,product = find_sum_and_product(array)
    print("The Array is : ",array)
    print(f"SUM = {sum} and PRODUCT = {product}")


