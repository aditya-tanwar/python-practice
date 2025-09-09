



# create the main function
def main():
    playback_speed()

# create the function 
def playback_speed():
    x = input()
#print(x, sep='...') 
# # this will not work as it will take multiple objects to be able to use sep
    # create the logic 
    print(x.replace(" ", "..."))

main()

