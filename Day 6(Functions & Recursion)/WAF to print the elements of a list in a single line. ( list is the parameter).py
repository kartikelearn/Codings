#WAF to print the elements of a list in a single line. ( list is the parameter)
def print_el(list=[1,2,3,4,5]):
    i=0
    while(i<len(list)):
        print(list[i], end=" ")
        i+=1
print_el()

def print_el1(list=[1,2,3,4,5]):
    for el in list:
        print(el,end=" ")
print_el1()