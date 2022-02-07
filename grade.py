score1=int(input("Enter math"))
score2=int(input("Enter english"))
score3=int(input("Enter art"))
score4=int(input("Enter chem"))
score5=int(input("Enter science"))
average=(score1+score2+score3+score4+score5)/5
if average>=70 and average<=100:
    print("Grade A")
elif average>=60 and average<=69:
    print("Grade B")
elif average>=50 and average<=59:
    print("Grade C")
elif average>=40 and average<=49:
    print("Grade C")
else:
    print("Fail")