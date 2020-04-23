import random 

def gameSystem(limit, count):
    number = random.randint(1, count)
    chances = limit

    for x in range(limit):
      
        guess = int(input())
        chances -= 1    
     
        if guess == number: 
          
            print("Congratulation YOU WON!!!") 
            break
        else:
            print("That was wrong", guess)
            print("number of chances", chances)                
       
    else:
        print("GAME OVER!!! The number is", number)
    
  
print("Number guessing game")
print("Select a difficulty level: ")
print('A - EASY(6 chances range is between 1-10)')
print('B - MEDUIM(3 chances range is between 1-20)')
print('C - HARD(1 chance range is between 1-50)')
difficulty  = (input())

if difficulty == 'A':
    print("Guess a number (between 1 and 10):")
    gameSystem(6, 10)
    
elif difficulty == 'B':
    print("Guess a number (between 1 and 20):")
    gameSystem(4, 20)

elif difficulty == 'C':
    print("Guess a number (between 1 and 50):")
    gameSystem(3, 50)

else:
    print("wrong selection please start over")
