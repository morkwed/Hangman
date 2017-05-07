print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |   O              By: Dustin Morkwed')
print(' |  \|/')
print(' |  / \ ')
print(' |              PRESS ENTER TO BEGIN')
print('=========')
from random import randint
import time
import string
global state
state = 0
global guesses
guesses = ''

input()
words = ['remote', 'shoe', 'pizza', 'fish', 'Raspberry', 'linix', 'kitten', ]


word = words[randint(0,len(words)-1)]
s_word = word.replace("", " ")
s_word = s_word.upper()
global letters
letters = '#'*len(word)
letters = letters.replace(""," ")
wod = "E"
global s_letters
s_letters= letters
global x
x = 0

global outy
outy = ''



def gallows():
    
    print('\n' *50)
    #print(s_word)
    #outy = [pos for pos, char in enumerate(s_word) if char == wod]
    #print (outy)
   #s_letters =list(letters)
    #global x
    #x = 0
    #while outy[x] < outy[-1]:
     #   s_letters[outy[x]] = s_word[outy[x]]
      #  x=x+1
    #else:
     #   s_letters[outy[-1]] = s_word[outy[-1]]
    #s_letters = "".join(s_letters)
    #print(s_letters)
    
    print(' _____  '+ str(guesses))
    print(' |   | ' )
    if state == 0:
        print(' | ')
    else:
        print(' |   O ')
    if state <2:
        print(' | ')
    elif state == 2:
        print(' |   | ')
    elif state == 3:
        print(' |  \| ')
    elif state >= 4:
        print(' |  \|/')
    if state <= 4:
        print (' | ')
    elif state == 5:
        print(' |  /  ')
    elif state == 6:
        print(' |  / \   GAME OVER')
    print (' |                     ' + str(s_letters))
    print('=========               ' + '_ '* len(word) )

while state < 7:
    gallows()
    letter = input('Please Choose A Letter:')
    if len(letter) == 1:
        if letter.isalpha():
            if letter.upper() not in guesses:
                guesses = guesses + letter.upper()
                if letter.upper() in word.upper():
                    #letters = letters +letter.upper()
                    outy = [pos for pos, char in enumerate(s_word) if char == letter.upper()]
                    while outy[x] < outy[-1]:
                        s_letters =list(s_letters)
                        s_letters[outy[x]] = s_word[outy[x]]
                        x=x+1
                    else:
                        s_letters =list(s_letters)
                        s_letters[outy[-1]] = s_word[outy[-1]]
                        s_letters = "".join(s_letters)
                        x=0
                    pass
                else:                    
                    state = state+1
            else:
                print('You already guessed ' + str(letter))
                time.sleep(1)
        else:
            print(str(letter) + ' is not a valid letter')
            time.sleep(1)
    else:
        print(str(letter) + ' is more than one letter')
        time.sleep(1)
    if state == 6:
        s_letters =s_word
    
        print('\n' * 50)
        gallows()
        again = input('Press "y" to play again.')
        if again == "y":
            state = 0
            guesses = ""
            
            word = words[randint(0,len(words)-1)]
            letters = '#'*len(word)
            letters = letters.replace(""," ")
            s_letters = letters
            s_word = word.replace("", " ")
            s_word = s_word.upper()
        else:
            state = state +1
            print('Bye')
            time.sleep(2)
    elif s_word == s_letters:
        print('\n' *50)
        gallows()
        again = input('You Won! Press "y" to play again!')
        if again == "y":
            state = 0
            guesses = ""

            word = words[randint(0,len(words)-1)]
            letters = '#'*len(word)
            letters = letters.replace(""," ")
            s_letters = letters
            s_word = word.replace("", " ")
            s_word = s_word.upper()
        else:
            state = 7
            print('Bye')
            time.sleep(2)

print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |   O              By: Dustin Morkwed')
print(' |  \|/')
print(' |  / \ ')
print(' |              ')
print('=========')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |   O ')
print(' |  \|/ ')
print(' |  / \         ')
print('=========')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |    O ')
print(' |   /|\ ')
print(' |   / \         ')
print('=========')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |      O ')
print(' |     /|\ ')
print(' |     / \         ')
print('=========')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |        O ')
print(' |       /|\ ')
print(' |       / \         ')
print('=========')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |        O  ')
print(' |       /|\         ')
print('=========/ \       ')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |          O  ')
print(' |         /|\         ')
print('=========  / \       ')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |            O  ')
print(' |           /|\         ')
print('=========    / \       ')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |              O  ')
print(' |             /|\         ')
print('=========      / \       ')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |                O  ')
print(' |               /|\         ')
print('=========        / \       ')
time.sleep(0.1)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |                O -Bye! ')
print(' |               /|\         ')
print('=========        / \       ')
time.sleep(0.5)
print('\n'*50)
print(' _____')
print(' |   |          HANGMAN')
print(' |                  By: Dustin Morkwed')
print(' |         ')
print(' |                ')
print(' |                       ')
print('=========              ')
time.sleep(0.1)


                
            
        
        
