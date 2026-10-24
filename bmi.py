txt = 'Addis Ababa University'


''' Body mass index CALCULATOR'''
print("BMI calculator \n")

weight = input("Enter weight (KG) : ")
height = input("Enter height (m) : ")
print("Your weight : ",weight)
print("Your height : ",height)

w=float(weight)
h=float(height)
bmi=w/(h*h)

if bmi<=18:
    print("===== Under weight: ",bmi," ======")
elif bmi<25:
    print("===== Normal : ",bmi," =====")
else:
    print("==== Over weight: ",bmi," =====")


