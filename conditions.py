
var = 100
if var == 200:
   print ("1 - Got a true expression value")
   print (var)
elif var == 150:
   print ("2 - Got a true expression value")
   print (var)
elif var == 100:
   print ("3 - Got a true expression value")
   print (var)
else:
   print ("4 - Got a false expression value")
   print (var)

print ("Good bye!")


#Nested


coursework = "English"
score_theory = 53
score_practical = 35

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50):
        print("Please check the input score for 'Science: Theory'.")
    elif(score_practical > 50):
            print("Please check the input score for 'Science: Practical'.")  
    else:
        print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60):
        print("Please check the input score for 'English: Theory'.")
    elif(score_practical > 40):
            print("Please check the input score for 'English: Practical'.")  
    else:
        print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")
