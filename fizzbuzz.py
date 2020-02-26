#Ask for first player
print("Who should go first, C for the computer or U for the user?")
firstPlayer = input()
#Store user response and error catching
while(firstPlayer != 'C' and firstPlayer != 'U'):
    firstPlayer = input("Sorry, enter C for computer or U for user, be careful of capitals : ")

#ask user for how many numbers to count
print("How many numbers would you like to go up to? :")
maxNo = int(input())
#Outputs the amount of numbers to user
print("let's start with",  maxNo)
def compOutput(loop):
    #prints Fizz if it's a multiple of 3
    if loop%3 == 0 and loop%5!=0:
        print("Fizz")
    #prints Buzz if it's a multiple of 5
    elif loop%5 == 0 and loop%3!=0:
        print("Buzz")
    #prints FizzBuzz if it's a multiple of both!
    elif loop%5==0 and loop%3==0:
        print("FizzBuzz")
    else:
        #prints the loop index if not multiple of 3 or 5
        print(loop)
def compStart():
    #loop starting at 1 up to predefined amount of numbers
    for loop in range(1,maxNo+1):
        #computer starts so does all odd numbers, starts at 1
        if loop%2 != 0:
            compOutput(loop)
        else:
            #gets input from user
            number = input()
            #checks if user entered the loop number
            if(number==str(loop)):
                #if loop is a multiple of 3, user should say "fizz"
                if(loop%3 == 0):
                    print("Fail, loop is multiple of 3")
                    break;
                if(loop%5==0):
                    print("Fail, loop is a multiple of 5")
                    break
                pass
            else:
                if(number=="Fizz"):
                    if(loop%3==0 and loop%5!=0):
                        pass
                    else:
                        print(loop, "is not a multiple of 3!")
                        break
                elif(number=="Buzz"):
                    if(loop%5==0 and loop%3!=0):
                        pass
                    else:
                        print(loop, "is not a multiple of 5!")
                elif(number=="FizzBuzz"):
                    if(loop%3==0 and loop%5==0):
                        pass
                    else:
                        print(loop," is not a multiple of both!")
                        break
                else:
                    print("Number incorrect")
                    break


def userStart():
    number = int(input("Start by saying your number : "))
    if number!=1:
        print("The first number is 1!")
    else:
        pass
    for loop in range(2,maxNo+1):
        if loop%2 == 0:
            compOutput(loop)
        else:
            number = input()
            if(number==str(loop)):
                if(loop%3==0 and loop%5!=0):
                    print("Number is multiple of 3!")
                    break
                if(loop%5==0 and loop%3!=0):
                    print("Number is multiple of 5!")
                    break
                pass
            else:
                if(number=="Fizz"):
                    if(loop%3==0 and loop%5!=0):
                        pass
                    else:
                        print(loop, "is not a multiple of 3!")
                        break
                elif(number=="Buzz"):
                    if(loop%5==0 and loop%3!=0):
                        pass
                    else:
                        print(loop, "is not a multiple of 5!")
                elif(number=="FizzBuzz"):
                    if(loop%3==0 and loop%5==0):
                        pass
                    else:
                        print(loop," is not a multiple of both!")
                        break
                else:
                    print("Number incorrect")
                    break



if(firstPlayer == 'U'):
    userStart()
elif(firstPlayer == 'C'):
    compStart()
