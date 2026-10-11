import json

with open("talaba.json","r") as f:
    data=json.load(f)

print(f"Talaba: {data["ism"]} Bali: {data["ball"]}")