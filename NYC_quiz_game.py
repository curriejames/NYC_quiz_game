import sys 

print()
print("Welcome to my New York City quiz!\n")

playing = input ("Do you want to play? yes/no\n\n ")

if playing.lower() != "yes":
    print("Have a good day goodbye ") 
    sys.exit()

print("Okay let's play :) ")
   
score = 0  
    
    
answer = input("where was Seneca Village located? ")
if answer.lower() == "central park":
    print('Correct')
    score += 1
else:
    print('Incorrect')    
        

answer = input("Where is M42 located? ")
if answer.lower() == "grand central":
    print('Correct')
    score += 1
else:
    print('Incorrect') 


answer = input("Which borough is Columbia University in?  ")  
if answer.lower() == "manhattan": 
    print('Correct')
    score += 1
else:
    print('Incorrect')  


answer = input("What is New York State's flower? ")
if answer.lower() == "rose":
    print('Correct')
    score += 1
else:
    print('Incorrect') 


answer = input("What is New York State's bird? ")
if answer.lower() == "eastern bluebird":
    print('Correct')
    score += 1
else:
    print('Incorrect') 


answer = input("Which park has a trap door that leads to an 'enormous power vault' used to power the Winter Village? ")
if answer.lower() == "bryant park":
    print('Correct')
    score += 1
else:
    print('Incorrect') 


answer = input("Which park has a estimated 20,000 corpses that are still underneath the park? ")
if answer.lower() == "washington square park":
    print('Correct')
    score += 1
else:
    print('Incorrect')         

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 7) * 100) + "%.")
    
