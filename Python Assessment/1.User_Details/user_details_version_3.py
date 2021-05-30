#Define the function, the variable will be called name

def user_details(name):
    print("Hello", name,)

#Determine if the input only consists of string, if no ask user to input only letters
while True:
    name = input("Please Enter Your Name : ").capitalize()
    if name.isalpha():
        break
    
    else:
        print("Please Enter Only Letters")
     

#call the function
user_details(name)
