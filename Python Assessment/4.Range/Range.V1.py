#create a function, the variable name is rounds
def rounds():
  while True:
    r = int(input("Please enter the number of questions you would like to answer between 1-10: "))
    #determine if r is within range
    if 0<r<=10:
      break

 #if not then code loops
    else:
      print("Please enter numbers 1-10 only")

#call function
rounds()


