name_string = "Gaurav Patkari" #string = text eclosed in single or double quotes
print (name_string)

message1 = '"Beautifull is better than ugly." Said Faster'
print(message1)
message2 = 'It\'s also a valid string'
print(message2)

help_msg = '''            
usage: mysql command 
-h hostname 
-d datatbase name 
-u username 
- p password  
'''
print(help_msg)            #triple quote used to write and print the long message or text 


#Using Variables in String with f-strings 
name = "Team Shadow"
msg = f'Hii {name}'         #this use to put the value of variable in a string if needed 
print(msg)


 #Concatenate Python String 
greeting= "Good"
time = "Morning"
greeting = greeting + time + "!"
print(greeting) 


#Accessing String Elements
str1 = 'Python String'
print(str1[0])                  #here first declare the variable name then no. element that want to access 
print(str1[1])

print(str1[-1])                 #negative accessing the elements fromt the back side of string
print(str1[-3])


#Python String are Immutable that means we can't change or modify once declare the string 
str2 = "Python Program"
new_string = 'First ' + str2[0] + str2[1] + str2[2] + str2[3] + str2[4] + str2[5] + str2[6] + str2[7] #Modification in Immutable string is possbile but need to create a new one from the existing string
print(new_string)




