# Python code to demonstrate 
# to get characters from string

#using re.split

import re 

# initialising string 
ini_string = "123()#$ABGFDabcjw"
ini_string2 = "abceddfgh"

# printing strings 
print ("initial string : ", ini_string, ini_string2) 

# code to find characters in string 
res1 = " ".join(re.split("[^a-zA-Z]*", ini_string)) 
res2 = " ".join(re.split("[^a-zA-Z]*", ini_string2)) 

# printing resultant string 
print ("first string result: ", str(res1)) 
print ("second string result: ", str(res2)) 



#using re.fidall

import re 

# initialising string 
ini_string = "123()#$ABGFDabcjw"
ini_string2 = "abceddfgh"

# printing strings 
print ("initial string : \n", ini_string, "\n", ini_string2) 

# code to find characters in string 
res1 = " ".join(re.findall("[a-zA-Z]+", ini_string)) 
res2 = " ".join(re.findall("[a-zA-Z]+", ini_string2)) 

# printing resultant string 
print ("first string result: ", str(res1)) 
print ("second string result: ", str(res2))


#using isalpha()
# if present 

# initialising string 
ini_string = "123()#$ABGFDabcjw"

# printing string and its length 
print ("initial string : ", ini_string) 

# code to find characters in string 
res1 = "" 
for i in ini_string: 
	if i.isalpha(): 
		res1 = "".join([res1, i]) 


# printing resultant string 
print ("first result: ", str(res1)) 


