import json

with open("python/baholar.json","r") as f:
    data=json.load(f)

eng_yuqori=0
eng_yuqori_ism=""

for ism,baholar in data.items():
    ballar=sum(baholar)/len(baholar)
    print(f"{ism}: {ballar:.2f}")
    if ballar>eng_yuqori:
        eng_yuqori=ballar
        eng_yuqori_ism=ism

print(f"Eng yuqori o'rtacha: {eng_yuqori_ism}")
