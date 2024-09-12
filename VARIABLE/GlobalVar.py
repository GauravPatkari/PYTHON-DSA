#Local Variable :- Local variable in python are those which are initialized inside a function and belong only to that particular function. 
                   #it cannot be accesed anywhere ouside the funciton. 
def f(): 
    loc = "Local Variable Value"
    print("Inside the function", loc)
   
f()




#Global Variables :- The variables whci are defined outside any function and which are accessible throughout the program that is inisde and outside of every function. 

def f(): 
    print("Inside Function", gvar)           #Here we can access the variable thoughout the program

gvar = "Team Shadow Global"
f() 
print("Outside Function", gvar)




''' #GloblaL Keyword:- It used to declare that a variable inside a function as Global for further use in the program.
                       It exists in the global scope. As we know variables declared inside a function are local
                       to that function. Using the 'global' keyword we can modify a variable ouside the function of the current scope. 
''' 
 #Without Global Keyword

without_glo_keyword = "It can be used anywhere in the program" 
def without_global_function(): 
    print(without_glo_keyword)

without_global_function()



#With Global Keyword
'''
def with_global_function():
    global with_glo_keyword
    with_glo_keyword = "It can also used anywhere in the program after using Global Keyword even it will decalare inside the function"
    print("Inside the Function - ", with_glo_keyword)

with_global_function
print("Outside the Function for printing - ", with_glo_keyword)
'''









    


