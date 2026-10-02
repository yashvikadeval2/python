#copy one file to another file

f=open("file1.txt","r")
f1=open("file2.txt","r")

for i in f:
    f1.write(i)

f.close()
f1.close()