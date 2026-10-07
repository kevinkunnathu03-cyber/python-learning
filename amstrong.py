# check if a number amstrong or not
num=1
def count(num):
    count=0
    while num>0:
        count=count+1
        num=num//10
    return count


def amstrong(num):
    original_num=num
    sum=0
    c=count(num)
    while num>0:
        b=num%10
        sum=sum+b**c
        num=num//10
    if original_num==sum:
        return True
    else:
        return False
print(amstrong(num))
        


