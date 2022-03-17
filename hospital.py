patient1Name = "David Muthui"
Patient1Age = 24
patient1IDNO = 35153705

patient2Name = input("Enter Your Name")
patient2Age = input("Enter your Age")
patient2IDNO = input("Enter your ID NUmber")

if int(patient1IDNO) == int(patient2IDNO):
    print("Patient already Exists")
else:
    print("This is a new Patient")
