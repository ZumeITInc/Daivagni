# 11 wap input total marks
stud_name = input("Student name:")
roll_no = int(input("roll no:"))
s1=int(input("telugu:"))
s2=int(input("hindi:"))
s3=int(input("english:"))
s4=int(input("maths:"))
s5=int(input("science:"))
s6=int(input("social:"))


tm = s1+s2+s3+s4+s5+s6

# applying if condition
if tm > 360:
    print("1st class")
if tm>=300 and tm<360:
    print("second class")
if tm<300:
    print("Third class")
if tm<210:
    print("you are fail the exam")
print("Thankyou")


#given two int  values,return their sum.unless the two values are the same,then return double their sum
a=int(input("1stno"))
b=int(input("2nd no"))
sum=a+b
if a==b:
    print("sum=",sum+sum)
else:
    print(sum)
print("thanks")

