# Get fibonacci series using generator
def fib():
    num1,num2 = 0,1 
    while True:
        yield num1
        num1,num2 = num2,num1+num2
        
obj = fib()
for i in range(10):
    print(obj.__next__(),end=" ")
