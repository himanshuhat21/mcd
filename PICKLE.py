import pickle
f = open('bin)file.dat','rb')
dict1 = pickle.load(f)
f.close()
print(dict1)