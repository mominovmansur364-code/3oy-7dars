n=int(input("nechta talaba malumotini yozasiz: "))

talabalar=[]

for i in range(n):
    qator=input().split()
    ism=qator[0]
    yosh=qator[1]
    ball=qator[2]

    talaba={"ism":ism,"yosh":yosh,"ball":ball}
    talabalar.append(talaba)

with open("talabalar.txt","w") as f:
    for x in talabalar:
        f.write(f"{x['ism']} {x['yosh']} {x['ball']}\n")