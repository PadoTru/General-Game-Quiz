#importing random from python library to 'shuffle'
from random import shuffle

#using the rounds function to generate range
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
                                    print('Please enter an integer')

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
 #randomizing quiz
shuffle(quiz)
index = 0
optnum = 0

rounds()

print("We will now start the quiz!")
#printing randomized questions according to range
while r>0:
            data = quiz[0]
            q = data[0]
            data = data[1]
            answer = data['answer']
            choice = data['choice']

            print(q)
            print(choice)
            if r>0:
                        del quiz[0]
                        r-=1
                       

                        
