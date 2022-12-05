#3. Write a Python script to create a list of first N even natural numbers.
num=int(input("Enter any number to ...:"))
print([2*num-2*i for i in range(num)])
