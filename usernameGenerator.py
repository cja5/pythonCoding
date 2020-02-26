#gets the random module, allows us to use randint later
import random

#stores all the endings
endings = ["ing", "end", "axe", "gex", "goh"];


#asks user for number of students and stores it
noofstudents = int(input("What is number of students:"))

#loop for each student
for loop in range(noofstudents):
    
    #gets the first three letters
    first3 = str(input("Enter first 3 letters:"))
    
    #validation check - if input was not 3 letters, ask for it again
    while len(first3)!=3:
        first3 = str(input("Enter first 3 letters:"))
    
    #gets random integer between 0 and 5 and assigns it to variable x
    x = random.randint(0,5);

    #puts the two strings together using the first3 input and a random index of the array
    username = first3 + endings[x]

    #outputs username
    print(username)
