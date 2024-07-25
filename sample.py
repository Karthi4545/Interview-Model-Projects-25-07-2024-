print("**********INTERVIEW PROCESS*********")
job_type=["IT","NON-IT"]
application=input("Enter Your Job Type (IT OR NON-IT):")
if application in job_type:
    print(f"Karthi Technologies Hire {application} Jobs")
    if application=="IT":
        eligibility=["BE","B.TECH"]
        qualification=input("Enter Your Education :")
        if qualification in eligibility:
            experience_amount=6500
            salary_per_month=33000
            if qualification=="BE":
                experience=int(input("Enter Your Experience :"))
                total_experience=experience*experience_amount
                salary=total_experience+salary_per_month
                print("Congrats... You are Selected")
                print(f"Your salary per month is {salary} ")
            elif qualification=="B.TECH":
                experience=int(input("Enter Your Experience :"))
                total_experience=experience*experience_amount
                salary=total_experience+salary_per_month
                print("Congrats... You are Selected")
                print(f"Your salary per month is {salary} ")
        else:
            print("Sorry... Only Hire BE and B.TECH Students")
    elif application=="NON-IT":
        eligibility=["BBA","BCOM.CA","B.COM"]
        qualification=input("Enter Your Education :")
        if qualification in eligibility:
            experience_amount=2750
            salary_per_month=16000
            if qualification=="BBA":
                experience=int(input("Enter Your Experience :"))
                total_experience=experience*experience_amount
                salary=total_experience+salary_per_month
                print("Congrats... You are Selected")
                print(f"Your salary per month is {salary} ")
            elif qualification=="BCOM.CA":
                experience=int(input("Enter Your Experience :"))
                total_experience=experience*experience_amount
                salary=total_experience+salary_per_month
                print("Congrats... You are Selected")
                print(f"Your salary per month is {salary} ")
            elif qualification=="B.COM":
                experience=int(input("Enter Your Experience :"))
                total_experience=experience*experience_amount
                salary=total_experience+salary_per_month
                print("Congrats... You are Selected")
                print(f"Your salary per month is {salary} ")
        else:
            print("Sorry... Only Hire BBA, BCOM.CA and B.COM Students")
    else:
        print("Sorry... Only Hire IT and NON-IT")

else:
    print("Sorry.... Job Not Available")
