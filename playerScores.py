
#creates empty array
myarray = []
#initialises total
hittotal = 0;
total = 0;

#loops for each player, known value it was 6 on team
for loop in range(1,7):
    #asks for number of hits player number scored
    print("Enter number of hits player", loop, "scored:")
    #stores the above in hit
    hit = int(input())
    #validation check - makes sure hit is in range from 0-30 inclusive
    while (hit<-1 or hit>31):
        hit = int(input("out of range:"))
    #adds the number of hits for this player into the array
    myarray.append(hit)
    #adds the number of hits to the total
    hittotal = hittotal + hit;

#outputs the array then the hittotal
print(myarray)
print(hittotal)

#calculates average hits
ave_no = hittotal / 6
print(ave_no)

#checks for extra point if total hits is above 50
if(hittotal>50):
    print("You earned a point for totalling above 50")
    total = total + 1;
else:
    print("You did not earn a point for total")

#if average number of hits is above ten, give extra point
if(ave_no >= 10):
    print("You earned a point for your average")
    total = total + 1;
else:
    print("You did not earn the additional point")

#Outputs final totals
print("Team's final total is:" , total)
