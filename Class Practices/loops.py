#Loops

#loops are used TO print long list of numbers by a small code it keeps on repeatingthe same code again and again

#exmaple
i = 2
while i<20:
    print (i)
    i +=1 #i=i+1
 # and if the user wants to print these numbers in a single line put print(x,end=",") you can put dot comma or space and it will appear between the numbers 

#example 2 
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

 # Using the range Function with the for Loop
for x in range(0,20):
      print (x)

for x in range(15):
     print (x)

#Nested Loops is A loop withon a loop


#Nested loop
y= [5,8,10]
z=[9,7,3]
for c in y:
    for d in z:
        print (c,d)

# Another Example 

for a in range (4):   # 0,1,
    
      for b in range(1) :  #0,1,2
             print("outer loop" ,a , "Inner Loop" , b)