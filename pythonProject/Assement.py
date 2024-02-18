Name = input("What is your name? ")
a = int(input("Enter your height"))
print(a)
b = int(input("Enter your weight"))
print(b)
BMI=(b/a*2)
print('your BMI is',BMI,'kg/m2')
if BMI<18:
    print("Underweight")
elif BMI>=18 and BMI<=24:
    print("Normal")
elif BMI>=25 and BMI<=30:
    print("Overweight")
elif BMI>=30:
    print("Obese")




