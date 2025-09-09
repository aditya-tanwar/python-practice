

# create the main function
def main():
    m = int(input("Enter the mass in kg : "))
    e = einstein(m)
    print(e, "Joules")



# create the function
def einstein(mass=0):
    # create the logic
    c = int(300000000) ** 2 
    e = mass * c
    return e
    
    
main()


