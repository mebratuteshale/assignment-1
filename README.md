### Statistical Computing Git assignment
#### Introdution to Python

In python we use the `print` functions to send output to console and `input` function to get input from user.

The **BMI - calculator** illustrates the use of `print` and `input` python functions

```
print("BMI calculator \n")

weight = input("Enter weight (KG) : ")
height = input("Enter height (m) : ")
print("Your weight : ",weight)
print("Your height : ",height)

w=float(weight)
h=float(height)
bmi=w/(h*h)

if bmi<=18:
    print("---------- Under weight: ",bmi," ----------")
elif bmi<25:
    print("---------- Normal : ",bmi," ----------")
else:
    print("---------- Over weight: ",bmi," ----------")
```
### Run the bmi.py

Goto `Run` in the IDLE menu bar and select `Run module`

### Basic git commands
``` 
git status
git add
git commit
git push
git pull
```
