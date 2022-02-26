import random
user_win = 0
comput_win = 0
print()
options = ["rock","paper","scissors"]
while True:
    user_input = input("ENTER YOU PREFERNCE: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2)
    #rock = 0, paper = 1, scissor = 2
    comput_pick = options[random_num]
    print("COMPUTER PICKED IT'S ONE" ,comput_pick, ".")
    if user_input == 'rock' and comput_pick == 'scissors':
        print("YOU WON!")
        user_win+=1
    elif user_input == 'scissors' and comput_pick == 'paper':
        print("YOU WON!")
        user_win+=1
    elif user_input == 'paper' and comput_pick == 'rock':
        print("YOU WIN!")
        user_win+=1
    elif user_input == 'rock' and comput_pick == 'rock':
        print("NO POINTS!")
    elif user_input == 'paper'and comput_pick == 'paper':
        print("NO POINTS!")
    elif user_input == 'scissors' and comput_pick == 'scissors':
        print("NO POINTS!")
    else:
        print("YOU LOST! ALAS!")
        comput_win+=1
if comput_win> user_win:
    print("COMPUTER IS THE WINNER!!!")
elif comput_win< user_win:
    print("YOU WON THE GAME! WOW!")
else:
    print("SAME POINTS!")        
print("YOU WON",user_win ,"TIMES.")
print("COMPUTER WON",comput_win ,"TIMES.")
print("GOODBYE.\nTHAKS FOR PLAYING.\nCREDITS:-\nCREATOR:- HIMANSHU BISWAS.")
if comput_win> user_win:
    print("COMPUTER IS THE WINNER!!!")
elif comput_win< user_win:
    print("YOU WON THE GAME! WOW!")
elif comput_win == user_win:
    print("FITOOSS!!!")    
else:
    print("SAME POINTS!")
print("GO ON MY FRIENDS!!!")
print("CREATE SOMETHING NEW OF YOUR OWN!!!")    