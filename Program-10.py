#10. Develop any Rule based system for an application of your choice.
#Name : Nimavat Harita J.
#Enrollmrnt No: 92600584017

print("==============================")
print("career guidence system")
print("==============================")

c=input("do you like coding ?")
m=input("do you like maths ?")
b=input("do you like biology ?")
d=input("do you like drawing ?")

if c=="no" and m=="no" and b=="no" and d=="no":
    print("explore your interests and carrer options  further")
elif c=="no" and m=="no" and b=="no" and d=="yes":
    print("graphic designer/animator")
elif c=="no" and m=="no" and b=="yes" and d=="no":
    print("pharmasist/nurse")
elif c=="no" and m=="no" and b=="yes" and d=="yes":
    print("medical illustrator/healthcare educator")
elif  c=="no" and m=="yes" and b=="no" and d=="no":
    print("engineer/data analyst")
elif c=="no" and m==" yes" and b=="no" and d=="yes":
    print("architect")
elif c=="no" and m=="yes" and b=="yes" and d=="no":
    print("doctor")
elif c=="no" and m=="yes" and b=="yes" and d=="yes":
    print("medical illustrator/biomedical designer")
elif c=="yes" and m=="no" and b=="no" and d=="no":
    print("programer/web devloper")
elif c=="yes" and m=="no" and b=="no" and d=="yes":
    print("web designer/UI-UX designer")
elif c=="yes" and m=="no" and b=="yes" and d=="no":
    print("health app devloper")
elif c=="yes" and m=="no" and b=="yes" and d=="yes":
    print("medical illustrator")
elif c=="yes" and m=="yes" and b=="no" and d=="no":
    print("software engineer/computer scientist")
elif c=="yes" and m=="yes" and b=="no" and d=="yes":
    print("game devloper/UI engineer")
elif c=="yes" and m=="yes" and b=="yes" and d=="no":
    print("bioformaticsn scientist")
elif c=="yes" and m=="yes" and b=="yes" and d=="yes":
    print("biomedical software engineer/medical technology specialist")
else:
    print("explore another career of your interested area !\n")

print("thank you for using the career guidance export system!")

