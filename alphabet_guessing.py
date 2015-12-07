'''
this program plays a game about the alphabet and how well you know the what number corresponds to what leter, not just the order
MODE 1) display a letter of the alphabet and have the user enter the corresponing number (e.g a=1, y=25)
MODE 2) display a number and have the user enter the corresponing letter of the alphabet (e.g b=2, 26=z)
'''
import random   

def main():
    #element 0 is empty so my indexes are understandable by humans
    alpha_num = [ [], ['A',1], ['B',2], ['C',3], ['D',4], ['E',5], ['F',6], ['G',7], ['H',8], ['I',9], ['J',10], ['K',11], ['L',12], ['M',13], ['N',14], ['O',15], ['P',16], ['Q',17], ['R',18], ['S',19], ['T',20], ['U',21], ['V',22], ['W',23], ['X',24], ['Y',25], ['Z',26] ]

    print('This game tests how well you know the alphabet. A is the 1st letter so A=1. B is 2nd so B=2. Z is 26th, so Z=26. \nYou can play in 2 modes: guess the letter from the number, or guess the number from the letter.')
    again = 'Y'     #initialize 
    while again == 'Y': #the whole program runs in a loop which allows the user to change modes (or play again) if they want to 

        #also convert to upper case @ end of input
        guess_letter_or_num = input('\nEnter "L" to guess letters from numbers & "N" to guess numbers from letters: ').upper()
        proceed= False      #make sure they only enter L or N, so assume they failed
        if (guess_letter_or_num == 'L'):    # here are the 2 cases where i want to change the state to true and proceed
            proceed = True
        elif (guess_letter_or_num == 'N'):
            proceed = True
            
        while proceed == False:     #if they entered values other than L or N, make them enter it again
            guess_letter_or_num = input('You entered something other than "L" or "N". \nEnter "L" to guess letters from numbers & "N" to guess numbers from letters: ').upper()
            if (guess_letter_or_num == 'L'):
                proceed = True
            elif (guess_letter_or_num == 'N'):
                proceed = True            

#now we have the mode, we just check which one they wanted
        if (guess_letter_or_num == 'L'):    #letter mode
            print("Enter the letter corresponding to the number in the alphabet.  0 to exit")
            print(format('Number','10s'),format('Guess','10s') )    #print table headers
            guess='L'   #initialize guess to anythin other than '0' so loop goes @ lest once
            while guess != '0':     #testing if they entered '0' (as a string)
                rand_index = random.randint(1,26)   #this picks a random index
                print( format( alpha_num[rand_index][1], '5d'), end='') #print a letter. rand_index chooses the sub-list, 2nd index is 1 because we want to show the number
                guess = input('        ').upper()       #converts input to uppercase for easier comparison
                if guess !='0':     #print results as long as they didn't enter '0' to quit
                    if guess == alpha_num[rand_index][0]:   #compare user's guess to actual letter. NOTICE now using 0 for 2nd index 
                        print("Correct-----------")
                    else:       #show the real answer if they got it wrong
                        print("INCORRECT! Real answer:",alpha_num[rand_index][0])

        elif (guess_letter_or_num == 'N'):  #number mode
            print("Enter the number corresponding to the letter.  0 to exit")
            print(format('Letter','10s'),format('Guess','10s') )
            guess=1
            while guess != 0:       #this time it relies on the integer 0 as apposed to the string '0'
                rand_index = random.randint(1,26)
                print( "  " + alpha_num[rand_index][0], end='')     #format with min-width not working, so used string concatenation
                try:
                    guess = int(input('         '))      #this could cause the exception if they enter a string
                    if guess !=0:       #this time it relies on the integer 0 as apposed to the string '0'
                        if guess == alpha_num[rand_index][1]:
                            print("Correct-----------")
                        else:
                            print("INCORRECT! Real answer:",alpha_num[rand_index][1])
                except ValueError:      #error if they entered a non-integer
                    print("Incorrect data type! You likely entered text or a decimal. \nReal answer:",alpha_num[rand_index][1])
                    
        again=input('Change to other mode? Type "Y" for yes. Type anything else to quit: ').upper()  #do they want to play again & change mode?

    print("Finished")
main()
