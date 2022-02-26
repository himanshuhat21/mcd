import pickle
print("HELLO & WELCOME TO THE FILE MAKING & DELETING \n BY \n HIMANSHIU BISWAS")
while True:
    print("1.) DO YOU WANT TO MAKE FILE?")
    print("2.) DO YOU WANT TO DELETE IT?")
    choice = input("ENTER YOUR PREFERENCE: ")
    if choice == '1':
        file = open("himanshu.txt","w")
        file.write("YOUR FILE HAS BEEN CREATED!!!")
        file.write("CONGRATS")
        file.close()
    else:
        file.delete()
        print("YOUR FILE HAS BEEN DELETED.")    