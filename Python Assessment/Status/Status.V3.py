#create function
def status():

            #ask for user input, using .lower to convert input to lowercase
    status = input("\nAre you ready to play? \nPress y to continue or any other key to exit :  ").lower()

    #determine if user is ready
    if status == "y" or status == "yea" or status == "yes":
        print("\nWe will start shortly...")

        #any other input will exit the program
    else:
        print("\nThank you for taking the time to try out my quiz!")
        exit()

#call the function
status()
