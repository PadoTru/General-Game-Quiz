#create function
def status():

            #use while loop
            while True:
                        
                        #ask for user input
                status = input("\nAre you ready to play? \nPress y to continue or n to exit :  ")

                #determine if user is ready to play, if yes break loop, if no exit program
                if status == "y" or status == "Y" or status == "yes":
                    print("\nWe will start shortly...")
                    break
            
                if status == "n" or status == "N" or status == "no":
                    print("\nThank you for taking the time to try out my quiz!")
                    exit()
                    
                    #if user inputs anything else loop back
            else:
                        print("Please enter one of the options")

#call the function
status()
