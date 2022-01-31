#Program to give a discount when amount>=1000
>>> amount = float(input("Enter total amount:"))
Enter total amount:9999
>>> discount = 0.05*amount
>>> if amount>=1000:
...     print("discount is" ,discount)
... else:
...     print("No discount")
...
discount is 499.95000000000005
>>>