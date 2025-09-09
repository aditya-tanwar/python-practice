
obj = input("Enter the object: ")

# the match statement is similar to the switch statement in java / c or c++
match obj:
    case "A":
        print("A")
    case "B":
        print("B")
    case "C" | "D" | "E":
        print("Here is the case if it is C, D or E and you want to print same thing for all of them") 
    case _: # if the case is not handled then this will be executed 
        # case _ is used for default
        # it is used as 'else' statement in if-else
        print("If nothing else matters")