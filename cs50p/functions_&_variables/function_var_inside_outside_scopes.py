
# NOTE : RUN THE CODE snippets IN A SEPARATE FILE FOR BETTER VISIBILITY and UNDERSTANDING

# For example , lets say i have a function that prints a message 


def msg():
    message = "hello"
    print(f"The message inside the function is {message}")
msg()
print(f"The message outside the function is {message}")

# Now if I run the above code it will throw an error as the variable "message" is not defined outside the function

#-----------------------------------------------------------------------------------------------------------------

# There are 2 ways to solve this 
# 1) using a global variable
# 2) using a local variable

# lets see how to use a global variable

def msg_global():
    global message
    message = "hello"
    print(f"The message inside the function is {message}")
msg_global()
print(f"The message outside the function is {message}")

# Here you can also define the message variable outside the function as well like shown below

message = "hello"
def msg_global():
    print(f"The message inside the function is {message}")
msg_global()  
print(f"The message outside the function is {message}")


# Now the second way is to use a local variable and using the return statement to return the value so that it can be used outside the function

def msg_local():
    message = "hello"
    print(f"The message inside the function is {message}")
    return message
outside_msg = msg_local()
print(f"The message outside the function is {outside_msg}") 



# Also 


message = "Hello"
def msg_global():
    global message
    message = "Namaste" # this will either create the global variable if the variable is not defined outside the function
    # or it will update the value of the variable
    print(f"The message inside the function is {message}")
msg_global()
print(f"The message outside the function is {message}")