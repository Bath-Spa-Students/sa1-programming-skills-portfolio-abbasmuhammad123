# Decision Structures

revenue = int (input ("Enter Sales:"))#ask the user to enter their total revenue
bonus = 0 

# Check if revenue exceeds the threshold for a reward
if revenue >  90000:
     reward = 1000
else :
       reward = 0 # there will be No reward for revenue below the threshold
print ("Your Bonus is "+str(reward )) #print statement will show final output