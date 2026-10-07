a="X" \
"V"
values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
B=0
for i in range(len(a)):
    if i+1<len(a)and values[a[i]]< values[a[i+1]]:
        B-=values[a[i]]
    else:
        B+= values[a[i]]
print(B)