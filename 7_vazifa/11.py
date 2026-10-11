import json

with open("python/company.json","r") as f:
    data=json.load(f)

xodimlar=data["xodimlar"]

soni=len(xodimlar)
jami_oylik=0
dasturchilar=[]

for i in xodimlar:
    jami_oylik+=i["oylik"]
    if i["lavozim"]=="Dasturchi":
        dasturchilar.append(i)

ortacha_oylik=jami_oylik/soni

print(f"Xodimlar soni: {soni}")
print(f"Ortacha oylik: {ortacha_oylik:.2f}")

with open("python/dasturchilar.json","w") as f:
    json.dump(dasturchilar,f,indent=4)