#From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("D:\Codings\VS code python\Day 7(File I-O)\File sample.txt","r") as file:
    data=file.read()

    num=""
    for i in range(0,len(data),1):
        if data[i]==",":
            print(int(num))
            num=""
        else:
            num+=data[i]
    print(int(num)) # to print last number
    
        

#     nums=data.split(",")
#     for val in nums:
#         if(int(val)%2==0):
#             count+=1
# print(count)