from random import shuffle

lines1 = ('**********************************************************************')
lines2 = ('=========================================================')
lines3 = ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(lines1,"\nLet's Begin!")
def user_details():
            print(lines2,"\nHello", name, ". Welcome to Hafidz's General Game Quiz!\n"+lines2)
while True:
    name = input("Please Enter Your First Name: ").capitalize()
    if name.isalpha():
        break

    else:
        print(lines3, "\nPlease Enter Only Letters\n"+lines3)
       

def instructions():
            while True:
                        inst = input("\nWould you like to read the instructions?\na)yes\nb)no\nEnter here: ").lower()
                        if inst == "yes" or inst == "y" or inst == "yea" or inst == "a":
                                    print("\n"+lines2, "\nThe rules are simple. Answer the multi choice questions by entering (a/b/c/d).\nFor every question you get right you earn a point!\n"+lines2)
                                    break
                        if inst == "no" or inst == "n" or inst == "nah" or inst == "b" :
                                    break
                        else:
                                    print(lines3)
                                    print("Please enter the options")
                                    print(lines3)

def status():
            status = input("\nWould you like to play the quiz?\nEnter (y or yes) to continue or (any key) to exit the quiz : ").lower()
            if status == "y" or status == "yes":
                        print("Thank you, we shall begin shortly...")

            else:
                        print("Thank you for your time to visit my quiz! :)")
                        exit()

def rounds():
            global r, total
            while True:
                        try:
                          
                                    r = int(input("\nPlease enter the number of questions you would like to answer between 1-10: "))
                                    if 0<r<=10:
                                                break
                                    else:
                                                print(lines3,"\nPlease enter numbers 1-10 only\n"+lines3)
                        except:
                                    print(lines3,'\nPlease enter numbers only\n'+lines3)

            total = r

#using dictionaries in order to store the questions, choices, and answers
quiz = [
["=What is the best selling video game of all time?=",
 {'answer' : 'b', 'choice' : ' \na. Tetris \nb. Minecraft \nc. GTA V \nd. Call of Duty \n'}
 ],
["=Which of these consoles is the highest selling to date?=",
 {'answer' : 'a', 'choice' : ' \na. PS2 \nb. Nintendo DS \nc. PS4 \nd. Xbox\n'}
 ],
["=How many squares on a Chess board?=",
 {'answer' : 'c', 'choice' : ' \na. 49 \nb. 100 \nc. 64 \nd. 81\n'}
 ],
["=How many cards in a full deck of regular playing cards including the jokers?=",
 {'answer' : 'a', 'choice' : ' \na. 54 \nb. 52 \nc. 50 \nd. 48\n'}
 ],
["=Which of these are not a starter pokemon?=",
 {'answer' : 'd', 'choice' : ' \na. chimchar \nb. froakie \nc. bulbasaur \nd. charizard\n'}
 ],
["=Which game did Mario first appear in?=",
 {'answer' : 'c', 'choice' : ' \na. Mario Kart \nb. Super Mario \nc. Donkey Kong \nd. Apex Legends\n'}
 ],
["=Which of these is not the colour of one of the 4 pacman ghosts?=",
 {'answer' : 'c', 'choice' : ' \na. red \nb. orange \nc. yellow \nd. blue\n'}
 ],
["=What colour is the Pacman ghost named 'Blinky'?=",
 {'answer' : 'a', 'choice' : ' \na. red \nb. orange \nc. yellow \nd. blue\n'}
 ],
["=What year was overwatch released?=",
 {'answer' : 'd', 'choice' : ' \na. 2015 \nb. 2014 \nc. 2018 \nd. 2016\n'}
 ],
["=What is the name of the first ever video game?=",
 {'answer' : 'b', 'choice' : ' \na. Tetris \nb. Pong \nc. Space Invaders \nd. Pacman\n'}
 ],


]

shuffle(quiz)

index = 0
score = 0
optnum = 0

user_details()
instructions()
status()
rounds()

print("\n\n                                                "+lines1,"\n                                                                     HAFIDZ'S GENERAL GAME QUIZ\n                                                "+lines1)
print("(NOTE: At any time during the quiz, you can type 'xxx' to immediately exit the program)")
print("QUESTIONS")
while r>0:
            data = quiz[0]
            q = data[0]
            data = data[1]
            answer = data['answer']
            choice = data['choice']

            print("\n"+q)
            print(choice)
            while True:
                        user_answer = input ("Please enter one of the options (a/b/c/d): ").lower().replace(' ','')
                        if user_answer == 'xxx':
                          exit()
                          
                        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                                    if user_answer == answer:
                                                print("\n*************************************************************")
                                                print("      Great Job! You got it correct! Lets keep it up.")
                                                print("*************************************************************")
                                                              
                                                score +=1
                                                print("               |Your score is now", score,"|")
                                    else:
                                                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                                print("    Sorry! That's incorrect :( ... Nice Try! Let's going.")
                                                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                                
                                                print("               |Your score is still", score,"|\n")

                                    del quiz[0]
                                    r-=1
                                    break
                            
                          
                        else:
                                    print("Please enter the alphabet for chosen option")
print("\nYou have succesfully completed Hafidz's Game Quiz!")
print("Conragulations! "+name,", your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
  
print("\nThanks for playing")

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
                 


print("Thank you for the feedback!")
exit()
