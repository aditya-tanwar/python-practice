


def hello(name="user"): 
    # adding a default value , if the function is not passed in function calling the 
    # default value comes into play
    # all of the line that insid the identation will be considered as part of the hello function
    print(f"hello {name} , How are you?")


name = input("what is your name ? ")
hello(name)
