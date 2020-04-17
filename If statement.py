# 11 wap input total marks
sname=input("student name:")
roll_no=int(input("roll no:"))
s1=int(input("telugu:"))
s2=int(input("hindi:"))
s3=int(input("english:"))
s4=int(input("maths:"))
s5=int(input("science:"))
s6=int(input("social:"))
tm=s1+s2+s3+s4+s5+s6
if tm>360:
    print("1st class")
if tm>=300 and tm<360:
    print("second class")
if tm<300:
    print("Third class")
if tm<210:
    print("you are fail the exam")
print("thankyou")

