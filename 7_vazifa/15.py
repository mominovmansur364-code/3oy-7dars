import json
n=int(input("Nechta mahsulot kiritasiz: "))

mahsulotlar=[]

for i in range(n):
    mahsulot={"nomi":input("Nomi: "),"narxi":input("Narxi: "),"miqdori":input("Miqdori: ")}
    mahsulotlar.append(mahsulot) 

with open("mahsulotlar.json","w") as f:
    json.dump(mahsulotlar,f,indent=4)