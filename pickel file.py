def fOperation():
    import pickle
    list1 = [10,20,30,40,50]
    f = open ('list.dat','wb')
    pickle.dump(list1,f)
    print("LIST ADDED TO BINARY FILE.")
    f.close()
fOperation()    