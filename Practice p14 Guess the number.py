# -*- coding: utf-8 -*-

import random 

def guess(x):
    random_number = random.randint(1,x) 
    guess =0 

    while guess != random_number :
        guess = int(input (f'Guess a number between 1 and {x} : '))
        
        if guess < random_number:
            print('Sorry, you guessed TOO LOW !!')
            option = input ('Wanna try again ? (y/n) ' )
            if option.lower() == 'y':
                print('Sure, give another try...\n')
            else :
                print('OK')
                break 
                
        elif guess > random_number:
            print('Sorry, you guessed TOO HIGH !!')
            option1 = input ('Wanna try again ? (y/n) ' )
            if option1.lower() == 'y':
                print('Sure, give another try...\n')
            else :
                print('OK')
                break 
        elif guess == random_number:
            
            print(f'Oh yess, you are correctly on that number {random_number}. Congrats !!! ')

        
guess(15)
         
