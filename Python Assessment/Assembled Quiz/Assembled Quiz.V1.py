from random import shuffle

def user_details():
            print("Hello", name, ". Welcome to the Basketball Quiz!")
while True:
    name = input("Please Enter Your Name: ")
    if name.isalpha():
        break

    else:
        print("Please Enter Only Letters")


def instructions():
            while True:
                        inst = input("Would you like to read the instructions?\na)yes\nb)no\nEnter here: ")
                        if inst == "yes" or inst == "y" or inst == "A" or inst == "a":
                                    print("Rules r simple. Answer the multi choice questions by entering (a/b/c/d). For every question you get right you earn a point.")
                                    break
                        if inst == "no" or inst == "n" or inst == "B" or inst == "b" :
                                    print("Welcome to Isaac's basketball quiz")
                                    break
                        else:
                                    print("Please enter the options")

def status():
            status = input("Would you like to play the quiz?\n Enter y to continue or n to exit the quiz : ").lower()
            if status == "y" or status == "yes":
                        print("Thank you, we shall begin shortly...")
            else:
                        print("Thank you for taking the time to...")
                        exit()

def rounds():
            global r, total
            while True:
                        try:
                                    r = int(input("Please enter the number of questions you would like to answer between 1-10: "))
                                    if 0<r<=10:
                                                break
                                    else:
                                                print("Please enter numbers 1-10 only")
                        except:
                                    print('Please enter numbers only')

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
while r>0:
            data = quiz[0]
            q = data[0]
            data = data[1]
            answer = data['answer']
            choice = data['choice']

            print(q)
            print(choice)
            while True:
                        user_answer = input ("Please enter one of the options (a/b/c/d): ").lower().replace(' ','')
                        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                                    if user_answer == answer:
                                                print("Yeah u got it right!")
                                                score +=1
                                                print("Your score is", score)
                                    else:
                                                print("You got it wrong!")
                                                print("Your score is ",score)

                                    del quiz[0]
                                    r-=1
                                    break
                        else:
                                    print("Please enter the alphabet for chosen option")
print("You have succesfully completed Isaac's Basketball quiz!")
print(name,"Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")
feedback = input("How would you rate the quiz from 1-5?: ")
print("Thank you for the feedback!")
exit()
