def binflie():
    import pickle
    file = open('data.dat','wb')
    while True:
        x = int(input("ENTER THE INTEGER: "))
        pickle.dump(x,file)
        ans = input("DO YOU WANT TO ENTER MORE DATA(Y/N):")
        if ans.upper() == 'N': 
            break

    filele.close()
    file = open('data.dat','rb')
    try:
        while True:
            y = pickle.load(file)
    except EOFError:
        pass
    ytfile.close()
binflie()            