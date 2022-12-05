#2. Write a Python script to create a list of first N odd natural numbers.
num=int(input("Enter any number to create a list of odd first natural number...:"))
print([2*num-2*i-1 for i in range(num)])