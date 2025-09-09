

# THIS IS THE MAIN FUNCTION THAT IS CALLING ALL THE OTHER FUNCTIONS
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# accepts string as an input 
# $##.## 

def dollars_to_float(d):
    # It itself is going to show one value after the decimal example if the input is $50.00 it will show 50.0 instead of 50.00 as both are same.
    d = float(d.strip("$"))
    #print(d)
    return d


def percent_to_float(p):
     f_value = float(p.strip("%")) / 100
     #
     # print(f_value)
     return f_value

    


main()
