
# here i am storing the value of the input function inside the name variable
name = input("Hi good Morning, what is your name? ")

# here i am calling the name variable inside the print function using a ","
print("Hello " + name)

# this can also be done using "," instead of "+"

print("hello", name)

# If i dont want to use any of the above and always want to highlight my variables for better visibility 
# I can do this instead 

print(f"Hello, {name}")

# the "f" will format the line for us 



'''
As we know that each statement of the print statement ends with a newline
That behaviour can be changed by 
1) going through the print() function document 
2) adding a named parameter like below when using the print statement
'''

print("testing the print" , end=' ')
print("Functions")

'''
There are some built in functionalities ( known as methods ) that comes with the objects 
for example to be able to remove the whitespaces from left and right of the input string then 
name = name.strip() can be used here the objects.methods()
'''