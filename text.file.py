import pickle
file1 = open("himanshu.dat","wb")
while True:
    x = int(input("ENTER THE READINGS OF YOUR CHEM PRACTICAL: "))
    Y = input("ENTER YOUR NAME: ")
    ans = input("DO YOU WNAT ADD MOREV INFO. TO THE COMPUTER: ")
    pickle.dump(x,file1)
    if ans == 'N' or ans == 'no':
        file1.close()
        file1 = open('himanshu.dat','rb')
        try:
            while True:
                z = pickle.load(file1)
                print(z)
        except EOFError:
            pass
        file1.close()




