#This program was created by Orlando Lewis 
#This program should ask the user for the annually percentage increase in tuition at Community College of Aurora for 5 years 
#The name of this program is WIG 
#WIG is a tuition calculation program that uses a base tuition price that is written in the program and only can be change within the program
#WIG will ask the user only for the percentage increase and it will calculate the total amount for each year and at the end of the program,
#it will add each year and give a total to the user at the end of all 5 years.


#initializing variables
percentageIncrease=0.0
percent=0.0
tuitionI=0.0
tuitionT=0.0
totalTuition=0.0
cont="y"

#initializing constants
TUITION=3181.68
MAX=6
CONVERTER=100

#Giving the details of the program
print("********Welcome to WIG Software********")

print("\n\t\t\t\t Created by SWERF Tech")

print("__________________________________________________________________________")

print("\n\n\n*****School System: Community College of Aurora******")

print("\n>>>WIG is a tuition calculation program that uses a base tuition price that is \nwritten in the program and only can be change within the program.<<<")

print("\nThe Default Base Tuition is: $",TUITION,"\n")

print("\n>>>The program will ask you for the percentage increase; after you type the \nnumber press enter to conutinue.<<<")

print("\n>>>The program will run for five years and at the end it will gve you a \ntotal value of all years.<<<")

#An example of how the program should look like after the user enter the percentage increase
print("\nExample:")
print("Year: 1 \nTuition: n/a")

print("__________________________________________________________________________")
print("\n\n\n")



while (cont == "y" or cont=="Y"): # incase the user wants to use the program one more time at the end of this program it will ask. If the user input "y" it will run again and not run if the user input anything else
#Asking the user for information that will outputted at the end of the program
    studentName=input("Student's name:\n")


    studentNumber=int(input("Student Number(hint:S2108638): \nS"))

 
#Asking the user for the percentage increase
#Everytime the program repeats it will give the total amount for the particular year 
    for year in range(1,MAX):
        print("Year:",year) 
        percentageIncrease=float(input("What is the percentage increase for this year (in percentage):"))

       #If the user input anything below 0 or above 100 , the program will tell the user that it is an invalid percentage and to input a valid one..
        while (percentageIncrease <0 or percentageIncrease>100 ):
            print("\n***ERROR:INVALID PERCENTAGE INCREASE***")
            percentageIncrease=float(input("What is the percentage increase for this year (in percentage):"))

        percent= percentageIncrease /CONVERTER # Converting the percentage in decimals to use in the calculation

        tuitionI=TUITION *percent #Finding the how much the base tuition will increase by (the tuition increase)

        tuitionT= TUITION + tuitionI #Adding the tuition increase to the base tuition to find out the total tuition
       
        print("\nTuition: $",format(tuitionT,'.2f')) # displaying the tuition total after each year 
        print("\n")

        totalTuition+=tuitionT #adding all the tuition in each year to give a total amount after the 5 years . This will display at the end of the program 

        
        year+=1

    print("__________________________________________________________________________")

    #Displaying the total tuition for all the years, with the student name and student number.
    print("\nStudent Name:",studentName)
    print("Student S#:",studentNumber)
    print("Total Tuition is:")   
    print ("$",format(totalTuition,'.2f'))
    print("\n__________________________________________________________________________")
    cont=input("\nEnter \"y\" if you would like to use WIG again or \"n\" if not:") #Asking the user if he or she wants the program to run again
print("__________________________________________________________________________")
print("\n\n\n")
print("Thank you for using WIG Software by SWERF Tech.")



