# # To combine modes
# f=open("FDemo.txt","r+") # used for reading & writing doesn't trascribe the data, Overwrite data from starting
# f.write("Sex")   # Doesn't create a file
# f.close()

# f=open("FDemo.txt","w+") # The stream is positioned at 1st as like "r+", it's also used to read and write both
# f.write("Do Sex")
# f.seek(0)       # To move pointer at beginning
# data=f.read()
# print(data)
# f.close()

f=open("FDemo.txt","a+")
f.write("\nSex is really an Art")
f.seek(0)
print(f.read())
f.close()