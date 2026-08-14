#Write a recursive function to print all elements in a list.
def print_el(list=[1,2,3,4,5],n=0):
    if(n==len(list)):
       return 0
    else:
       # print_el(list,n+1)
        print(list[n])
        print_el(list,n+1)
print_el()

