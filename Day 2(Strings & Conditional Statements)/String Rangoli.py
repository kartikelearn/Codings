# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

size=int(input())
alphabets="abcdefghijklmnopqrstuvwxyz"
rows=[]
for i in range(size):
    s="-".join(alphabets[size-1:i:-1]+alphabets[i:size])
    rows.append(s.center(4*size-3,"-"))
print("\n".join(rows[::-1]+rows[1:]))