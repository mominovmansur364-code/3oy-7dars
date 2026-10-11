avtomobil={"marka":input(),"yili":input(),"narxi":input()}

with open("avtomobil.txt","w") as f:
    f.write(f"{avtomobil['marka']}\n")
    f.write(f"{avtomobil['yili']}\n")
    f.write(f"{avtomobil['narxi']}\n")