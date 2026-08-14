#Write a program to calculate the total salary of an employee if:
#Basic salary is input
# HRA = 20% of basic
# DA = 10% of basic
basic_salary=int(input("Enter Your Basic Salary: "))
Total_salary=basic_salary+((basic_salary*0.2)+(basic_salary*0.1))
print("The final salary of the worker is: ",Total_salary)
