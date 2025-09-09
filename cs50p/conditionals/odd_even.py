


def main():
    x = int(input("Enter the number : "))
    # we can also directly print the output of the function
    print(is_even(x))
    # can also be used as 
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 == 0: 
    #     print("even")
    #     return 0 
    # else:
    #     print("odd")
    #     return 1 
    
# there is also another way to do this 
    # return True if n % 2 == 0 else False ## this is a single statement if condition
    return n % 2 == 0 # can also write it as return (n % 2 == 0)

main ()
    