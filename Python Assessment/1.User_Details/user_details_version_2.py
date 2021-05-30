#create a function, the variable will be called name
def user_details(name):
    print("Hello", name)

#ask for user string input and print name
name = str(input("Enter your name : ")).lower()
print ("Your name is", name)

#call the function
user_details(name)

