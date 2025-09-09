


def main():
    x = input("What is the answer of The Great Question of Life, the Universe and Everything?")
    f1(x)
    
    
def f1(n):
    # if n == "42":
    #     print("Yes")
    # elif n == "forty-two":
    #     print("Yes")
    # elif n == "forty two":
    #     print("Yes")
    # else:
    #     print("No")

# We can also do it alternatively
    match n: # here is the object that we needs to match
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")
            
        
main()