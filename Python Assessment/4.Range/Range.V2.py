#create a function, the variable name is rounds
def rounds():

  #using number of rounds as total questions
            global r, total
            while True:
                        try:
                                    r = int(input("Please enter the number of questions you would like to answer between 1-10: "))

                                    #determine if r is within range
                                    if 0<r<=10:
                                                break

                                              #if not then code loops
                                    else:
                                                print("Please enter numbers 1-10 only")

                        #if user does not enter an integer, code loops                        
                        except:
                                    print('Please enter numbers only')

            total = r
            
#call the function
rounds()
