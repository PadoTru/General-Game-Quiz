#create function
def instructions():
            
            #use while loop
            while True:
                        
                        #ask for user input, using .lower to convert input to lowercase
                        inst = input("Would you like to read the instructions?\na)yes\nb)no\nEnter here: ").lower()
                        
                        #determine if user would like to read instructions
                        if inst == "yes" or inst == "y" or inst == "yea" or inst == "a":
                                    
                                    #If yes print instructions, if no continue without printing
                                    print("The rules are simple. Answer the multi choice questions by entering (a/b/c/d). For every question you get right you earn a point.")
                                    break
                        
                        if inst == "no" or inst == "n" or inst == "nah" or inst == "b" :
                                    break
                        else:
                                    #if user answer anything else, program will ask for one of the options
                                    print("Please enter the options")
                                    
#call the function
instructions()
