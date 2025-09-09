def msg_global():
    message = "hello"
    return message
    print(f"The message inside the function is {message}") # you can see this has automatically becomes disable because 
    # anything after the return statement is ignored 
    # because the return statement ends the function execution 
    
o_msg = msg_global()
print(f"The message outside the function is {o_msg}")