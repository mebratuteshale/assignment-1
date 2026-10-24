## Body Mass Index calculator
This project was created to learn the fundamentals of Git as part of the Statistical Computing course. It features a simple Body Mass Index (BMI) Calculator that accepts the user's weight and height as inputs, calculates their BMI, and displays the result.
The project provides an opportunity to practice basic Git operations, including repository creation, version control, commits, and pushing changes to GitHub.
### Features
Accepts the user's height and weight as strings, converts both values to floating-point numbers, calculates the BMI, and returns the resulting BMI value.
### Clone the git repo
To clone the project into local repo
1. create a folder `assignment-1` and navigate to the new directory
2. Open a `terminal` to the newly created directory and run the `git clone`
`git clone https://github.com/mebratuteshale/assignment-1/`

In python we use the `print` functions to send output to console and `input` function to get input from user.
### Pre-requisite
* check if python is installed by running `python --version`
### Project structure
* README file is documentation for the project
* bmi.py is the python script to calculate BMI
* screenshot of commits.png is an image showing the commit commands applied to the online repo.
  
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
### How to Run bmi.py

Goto `Run` in the IDLE menu bar and select `Run module`

### Author
Mebratu T.
