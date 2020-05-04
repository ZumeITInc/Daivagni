# input any 4 digit num and find out the difference of all digits
num=input("enter four digits number: ")
sub=0
s=len(num)
if s==4:
    for i in num[::1]:
        count=i
        next=num[i+1]
        sub+=int(count)-int(next)
    print(count)
else:
     print("it is not a four digits number")
