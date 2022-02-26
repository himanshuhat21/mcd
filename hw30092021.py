f = open('test.txt')
print("BEFORE READING: ", f.tell())
s = f.read()
print("AFTER READING: ",f.tell())
f.seek(0)

print("LET\'S START FROM THE BEGINING AGAIN: ",f.tell())
s = f.read(4)
print("FIRST 4 BYTES ARE: ",s)
print(f.tell())
s = f.read(3)
print("NEXT 3 BYTES ARE: ",s)
print(f.tell())YT
f.close()