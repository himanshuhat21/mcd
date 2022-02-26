score = 0
total_q = 5
ans = input("ENTER YOUR ANSWER DO YOU WANT TO PLAY OR NOT? ")
if ans == 'YES':
    print("WELCOME TO THE QUIZ WORL OF MUGHALS\n MADE BY HIMANSHU BISWAS")
    print("ARE YOU READY TOM GO!!!\n")
    print("NOW WE ARE STARTING OUR GAME!!!\n")
    print("NOW THERE ARE SOME RULES FOR THE GAME THAT YOU SHOULD KNOW ABOUT\n")
    print("1.) ALL THE ANSWERS YOU WILL PUT IT\'S FIRST ALPHABET SHOULD START FROM CAPITAL LETTER\n")
    print("2.) PUT NUMERIC VALUES WHERE WE WILL SUGGEST YOU\n")
    print("NOW WE ARE END WITH OUR RULES\t")
    quiz_1 = print("WHICH MUGHAL KING REIGN DURING THE SCALE FEMIN OF INDIA?")
    ans_quiz = input("enter you answer: ")
    if ans_quiz == 'Shah Jahan':
        print("correct!!answer")
        score +=10
    else:
        print("wrong!!!")
        score-=2
    quiz_2 = print("WHO WAS MALLICK-HINDUSTAN")
    ans_quiz2 = input("ENTER THE ANSWER: ")
    if ans_quiz2 =='Jodha Bai':
        print("correct answer!!!")
        score+=10
    else:
        print("incorrect answer!!!")
        score-=2
    quiz_3 = print("WHO WAS THE MOTHER OF AKBAR?")
    ans_quiz3 = input("ENTER YOUR ANSWER: ")
    if ans_quiz3 == 'Hamida Begum':
        print("HERE YOU GO!!! CORRECT ANSWER!!!")
        score+=10
    else:
        print("incorrect!!!")
        score-=2
    quiz_4 = print("WHOM DID BABUR DEFEATED IN PANIPAT?")
    ans_quiz4 = input("ENTER YOUR ANSWER: ")
    if ans_quiz4 == 'Ibrahim Lodhi':
        print("correct answer!!!")
        score+=10
    else:
        print("incorrect answer!!!")
        score-=2
    quiz_5 = print("WHOW WAS AKBAR/'S FINANCE MINISTER?")
    ans_quiz5 = input("ENETR YOUR ANSWER: ")
    if ans_quiz5 == 'Todar Mal':
        print("correct answer!!!")
        score+=10
    else:
        print("incorrect answer!!!")
        score-=2
    print("THANK YOU FOR PLAYING THE GAME\n MADE BY\n HIMANSHU BISWAS.")
    MARKS = (score/total_q)*10
    print("YOUR MARKS ARE",MARKS,"%")
else:
    print("THANKS FOR GIVING TIME!!! \n WILL MEET YOU LATER.")       