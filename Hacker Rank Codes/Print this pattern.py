#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 
#1st Arrow part
row=1
while(row<=5):
    column=1
    while(column<=4):
        if(column>=row):
          print("l",end="")
        column+=1 
    column=1
    while(column<row*2):
        if(column<=row*2-1):
          print("H",end="")
        column+=1
    print()
    row+=1

# Row part

row=6
while(row<=12):
   column=2
   while(column<=29-7):
        if(3<column<5*2-1):
          print("H",end="")
        else:
          print("l",end="")
        column+=1
   column=29-7
   while(column<=29):
        if(29-7<column<29-1):
          print("H",end="")
        else:
          print("l",end="")
        column+=1
   print()
   row+=1

#Cuboidal Part

row=13
while(row<=12+3):
   column=1
   while(column<=29):
        if(2<column<29-1):
          print("H",end="")
        else:
          print("l",end="")
        column+=1
   print()
   row+=1

#Opposite row part

row=16
while(row<=16+6):
   column=2
   while(column<=29-7):
        if(3<column<5*2-1):
          print("H",end="")
        else:
          print("l",end="")
        column+=1
   column=29-7
   while(column<=29):
        if(29-7<column<29-1):
          print("H",end="")
        else:
          print("l",end="")
        column+=1
   print()
   row+=1

#Last Part or Opposite row part

row = 20
while(row <= 24):
    column = 1
    while(column <= 29):
        if(column <= row): 
            print("l", end="")
        column += 1
    # count = 2*(25 - row) - 1
    column = 1
    while(column <= 11):
        if(column<=2*(25 - row) - 1):
          print("H", end="")
        # elif(2*(25 - row) +1):
        #    print("l",end="")
        column += 1

    print()
    row += 1


