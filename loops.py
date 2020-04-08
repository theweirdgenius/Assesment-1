#code for while loop
x=0    
while (x<4):
    print (x)
    x= x+1


#simple for loop
x=0 
for x in range (2,7):
    print (x)

#Use of for loop in string
Months = ["Jan","Feb","Mar","April","May","June"]
for m in (Months):
    print (m)

#Use break-statement in for loop
for x in range (10,20):
       if (x == 15): break
       print (x)

#Code for "enumerate function" with "for loop"
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
    print (i,m)     
      
# use the break and continue statements
for x in range (10,20):
    if (x == 15): break
    if (x % 5 == 0) : continue
    print(x)
