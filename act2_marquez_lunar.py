prelims,midterm,semis,finals = int(input("Prelims :")),int(input("Midterms :")),int(input("Semis : ")),int(input("Finals : "))
ave= (prelims+midterm+semis+finals)/4
print ("The average is ", ave)
if ave >=75:
    print ("Passed")
else:
    print ("Failed")
if ave <= 100 and ave >=99:
    print ("Equivalent Grade :A")
elif ave <= 98 and ave >=90:
    print ("Equivalent Grade :B") 
elif ave <= 89 and ave >=80:
    print ("Equivalent Grade :C")
elif ave <= 79 and ave >=71:
    print ("Equivalent Grade :D")
elif ave <= 70 and ave >=61:
    print ("Equivalent Grade :E") 
else:
    print ("Equivalent Grade :F")