print("Enter Marks Obtained in 3 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science : "))

sum = math+english+science
print("sum = " ,sum)

perc = (sum/300)*100

print("percentage= ", int(perc), end="%")