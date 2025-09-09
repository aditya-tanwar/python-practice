def main():
    x = input("Greetings: ")
    bank(x)
    
    
def bank(x):
    if x.startswith(("hello", "Hello")):
        print("$0")
    elif x.startswith(("h", "H")):
        print("$20")
    else:
        print("$100")
        
main()