#Making a variable for each question
Q1 = ("=What is the best selling video game of all time?=\na. Tetris \nb. Minecraft \nc. GTA V \nd. Call of Duty \n")
Q2 = ("=Which of these consoles is the highest selling to date?=\na. PS2 \nb. Nintendo DS \nc. PS4 \nd. Xbox\n")
Q3 = ("=How many squares on a Chess board?=\na. 49 \nb. 100 \nc. 64 \nd. 81\n")
Q4 = ("=How many cards in a full deck of regular playing cards including the jokers?=na. 54 \nb. 52 \nc. 50 \nd. 48\n")
Q5 = ("=Which of these are not a starter pokemon?=\na. chimchar \nb. froakie \nc. bulbasaur \nd. charizard\n")
Q6 = ("=Which game did Mario first appear in?=\na. Mario Kart \nb. Super Mario \nc. Donkey Kong \nd. Apex Legends\n")
Q7 = ("=Which of these is not the colour of one of the 4 pacman ghosts?=\na. red \nb. orange \nc. yellow \nd. blue\n")
Q8 = ("=What colour is the Pacman ghost named 'Blinky'?=\na. red \nb. orange \nc. yellow \nd. blue\n")
Q9 = ("=What year was overwatch released?=\na. 2015 \nb. 2014 \nc. 2018 \nd. 2016\n")
Q10 = ("=What is the name of the first ever video game?=\na. Tetris \nb. Pong \nc. Space Invaders \nd. Pacman\n")

#using a while loop for the quiz. This prints the question, asks for the users input and determines if the input is the same as answer.
while True:
            print(Q1)
            answer1 = input("Please enter one of the options a-d: ")
            if answer1 == 'b' or answer1 == 'B':
                        print("Yes that is correct!")
                        break
            else:
                        print("No that is incorrect")
                        break

while True:
            print(Q2)
            answer2 = input("Please enter one of the options a-d: ")
            if answer2 == 'a' or answer2 == 'A':
                        print("Yes that is correct!")
                        break
            else:
                        print("No that is incorrect")
                        break
while True:
            print(Q3)
            answer3 = input("Please enter one of the options a-d: ")
            if answer3 == 'c' or answer3 == 'C':
                        print("Yes that is correct!")
                        break
            else:
                        print("No that is incorrect")
                        break
#The quiz would continue the same as above
