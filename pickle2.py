import pickle 
dict1 = {'Python ':90,'Java ':95,'C++ ':85}
f = open('bin)file.dat','wb')
pickle.dump(dict1,f)
f.close()