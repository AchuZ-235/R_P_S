import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n :")
    computer = random.choices(['r','p','s'])
    if user == computer:
        print ("Its a tie \n")
    
    if (user == 'r' and computer == 's') or (user =='s' and computer == 'p') or (user == 'p' and computer == 'r'):
        print("You won!")

    else:
        print("U lost")
        
        
        
#Again

def again():
    again=input("Play again? : ")
    Yes = (["Yes","yEs","yeS","YEs","YeS","yES","YES","yes","OK","ok","Ok","oK","Yah","yAh","yaH","YAh","yAH","YaH","YAH","ys","Ys","yS"])
    No = (["No","NO","no","nO","Nah","nah","NAH","nAH","NaH","NAh"])
    for again in Yes:
        return play()

play()
again()