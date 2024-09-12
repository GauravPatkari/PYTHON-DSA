'''
TUPLE :- It is a collection of Python Programming objects much like a list.
         The sequesnce of values stored in a tuple can be of any type, and 
         they are indexed by integers.
         - Values of a tuple are syntactically separated by 'commas' which knowan as Parentheses.
         - Creation of Tuple wihtout the use of parentheses is know as Tuple Packing.
'''

Tuple1 = ()                      #Creating an empty Tuple  
print("Initial empty tuple: ")
print(Tuple1)


Tuple1 = ('Gaurav', 'Patkari')
print("\nTuple with the use of String: ")
print(Tuple1)


list1 = [1, 2, 4, 5, 6]           #Creating a Tuple with the use of List
print("\nTuple using List: ")
print(tuple(list1))


Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)