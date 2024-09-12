#LIST 
integer_list = [1, 2, 3, 4, 5] #list = ordered collection of items 
print (integer_list)           #here we enlist the interger number to print the list 


string_list = ["one, two, three, four, five"]
print (string_list)            #here we enlist the words/text to print the it 


mix_list = ["1, two, 3.0, four, 500"]
print (mix_list)               #here we make the mixed list to print various datatypes in it but to declare and print we should be add it in single/double quote 
 

Blank_list: ()        #we can also print blank list 

#Accessing elements form the list using Index number 
Access_elementlist = ["Gaurav", "Kiran", "Patkari"]

print("Accessing a element form the list")
print(Access_elementlist[0])
print(Access_elementlist[2]) 


# Accessing elemetns from a Multi-Dimensional list
Multi_Dimensionallist = ["Gaurav", "Kiran"], ["Patkari","Surname"]  #here first list 

print("Accessing a elements for Multi_Dimensionallist")
print(Multi_Dimensionallist[0][1])   #where first bracket indicates no.of list & 2nd bracket indicates elememt.no of that list 
print(Multi_Dimensionallist[1][0])   



#SIZE OF LIST len()
list1= []
print(len(list1))           #here we print the size of list where first use len then declare the "list-name" that we want to declare 

list2=["one", "two", "three", "four"]  
print(len(list2))


#INPUT OF LIST
#input_list = input("Enter elements (Space-Separated):") #the input function use to take the input form the predefined declared variable 
#lst = input_list.split()
#print ('The list is:', lst)

#n = int(input("Enter the size of list : "))
#lst = list(map(int, input("Enter the list content: ").strip().split()))[:n]     # here we can give the size of list and then add the elements with that specific size of list
#print('The list is:', lst) 


#APPEND METHOD 
List3=[]
print("Initial blank list: ")
print(List3)


List3.append(1)
List3.append(2)
List3.append(4)
print("\nList after addition of three elements in it : ")
print(List3)
 

for i in range(1, 4):
    List3.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List3)

List3.append((5,6))
print("\n List after addition of a Tuple: ")    # time complexity = 0(1)
print(List3)                                    # space complexity = 0(1)


List3.append(("Gaurav", "Patkari"))
print("\n List after addition of list: ")
print(List3)



#INSERT METHOD
List4 =[1,2,3,4,5]
print("Initial list: ")
print (List4)


List4.insert(3, 3.0)                                            #here we add an extra interger whereever we want 
List4.insert(6, "gaurav")                                       #here we add the string same as above 
print("\nList for performing Insert Operation: ")               #in this method we can add the elements in desired position 
print(List4)



#REMOVE METHOD :- Elements can be reomved from the List by sungi the buil-in remove() funciton but it'll only applies if elements are available in that List
RList = [1,2,3,4,5,6,7,8,9,10,11,12]     #Creating List
print("Initial List: " )                  #Print that crated list
print(RList)

RList.remove(5)
RList.remove(8)
print("\nList after Removal of two elements: ")
print(RList)
