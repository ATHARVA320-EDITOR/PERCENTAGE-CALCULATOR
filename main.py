print("Enter marks obtained in 4 subjects")
Maths = float(input("Maths:"))
English= float(input("English:"))
Science = float(input("Science:"))
Hindi = float(input("Hindi:"))
sum =  Maths+English+Science+Hindi
print("Total marks in all subjects are:", sum)
perc = (sum/320)*100
print(end="Percentage is = ")
print(perc)