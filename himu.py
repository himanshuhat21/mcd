with open("himu.txt","w") as r:
    r.write("THIS IS HIMANSHU \n")
    r.write("AND I AM WRITING FOR TEXT FILE.")
z = open("himu.txt","r")
print(z.read()) 
with open("himu.txt","a") as r:
    NAME = input("ENTER THE NAME: ")
    AGE = input("ENTER THE AGE: ")
    r.write(NAME+","+AGE)
Z = open("himu.txt","r")
print(Z.read()) 

