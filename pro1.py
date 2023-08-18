marks1=int(input("Enter Test 1 Marks:"))
marks2=int(input("Enter Test 2 Marks:"))
marks3=int(input("Enter Test 3 Marks:"))
minimum=min(marks1,marks2,marks3)
sumofbest2=marks1+marks2+marks3-minimum
avgofbest2=sumofbest2/2
print("Avarage of best Two :",avgofbest2)
