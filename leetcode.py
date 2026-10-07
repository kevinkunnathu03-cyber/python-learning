
coin_5=0
coin_10=0
coin_20=0
dollar=[5,5,5,10,20]

for i in dollar:
    if i==5:
        coin_5=coin_5+1
        i=i+1
        
    
    elif i==10:
        coin_10=coin_10+1
    else:
        coin_20=coin_20+1
# print(coin_5,coin_10,coin_20)
flag=True
for i in dollar:
    if i==5:
        pass
    elif i==10:
        if coin_5>0:
            coin_5=coin_5-1
        else:
            flag=False
    else:
        if coin_10>0 and coin_5>0:
            coin_10=coin_10-1
            coin_5=coin_5-1
        elif coin_5>0:
            if coin_5>=3:
                coin_5=coin_5-3
            else:
                flag=False
if flag==True:
    print(True)
else:
    print(False)




    