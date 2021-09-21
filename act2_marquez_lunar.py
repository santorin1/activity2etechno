prelims,midterm,semis,finals = int(input("Prelims :")),int(input("Midterms :")),int(input("Semis : ")),int(input("Finals : "))
ave= (prelims+midterm+semis+finals)/4
print ("The average is ", ave)
if ave >=75:
    print ("Passed")
else:
    print ("Failed")