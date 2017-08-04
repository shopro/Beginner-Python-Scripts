import random
import time

balance = 100
spins = 0
guess = 0


while guess != "exit":
    number = random.randint(0,36)
    guess = input("Welcome to roulette, what number would you like to place a bet on? Type 'exit' to leave     ")
    if guess == "exit":
        print "Thanks for playing, your final balance is",balance,"and have stayed for",spins,"plays"
        break
    if guess > 36 or guess < 0:
        print "That number is not on the table"
    else: 
         print 'You have',balance,"remaining"
         bet = input("How much would you like to bet?     ")
         if bet > balance:
             print "You don't have enough money for that bet"
             
        
    
    
    
   
    if 0 < bet <= balance and 0 <= guess <= 36:
        print "You have bet",bet   
        guess = int(guess)
        spins += 1
        print '**Spinning**'
        time.sleep(3)
        if guess == number:
            print "Congratulations, it landed on",number,", you win!!"
            balance += bet*36
            print "Your new balance is",balance
            
        else:
            print "Sorry, it landed on",number,", better luck next time"
            balance += -bet
            if balance > 0:
                print "Your new balance is",balance
            else:
                print "Sorry, you are out of cash"
                break
