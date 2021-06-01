#conragulating the user for completing the quiz and thanking them
print("\nYou have succesfully completed Hafidz's Game Quiz!")
#displaying the score and percentage (performance)
print("Conragulations! "+name,", your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
  
print("\nThanks for playing")
#creating a function to ask for feedback
def feedback():
  while True:
    try:
      f = int(input("How would you rate the quiz from 1-5?: "))
      if 0<f<=5:
        break
      else:
        print("\n"+lines3,"\nPlease enter numbers 1-5 only\n"+lines3)
        
    except:
      print("\n"+lines3,'\nPlease enter numbers only\n'+lines3)
feedback()
                 

#thanking user for feedback and exiting quiz
print("Thank you for the feedback!")
exit()
