#NESTEDIF

salary=int(input("enter your salary;"))
if salary >= 50000:
    years_on_job= float(input("enter the years of job: "))
    if years_on_job>=2:
        print("you qualify for your job")
    else:
        print("experience is less than 2 years")

else:
    print("you earn atleast 30k to qualify") 
