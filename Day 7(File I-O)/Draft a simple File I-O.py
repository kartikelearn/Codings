# #Python can be used to perform operations on a file(read or write)
f=open("D:\Codings\VS code python\Day 7(File I-O)\Kartike.txt","r")
data=f.read(6)
print(data)
# data=f.readline()
# print(data)
f.close()

# Overwrite using "w"
f=open("D:\Codings\VS code python\Day 7(File I-O)\Kartike.txt","w")
f.write("I love Coding")
f.close()

# Append using "a"
f=open("D:\Codings\VS code python\Day 7(File I-O)\Kartike.txt","a")
f.write("\nI like building my Logics")
f.close()

# If there is no file exist of your name then Python automatically creates a file named that e.g.,
file=open("FDemo.txt","w")
file.close()
file=open("FDemo.txt","a")
file.write("My name is Kartike.")

