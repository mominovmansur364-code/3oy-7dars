talaba={"ism":input(),"yosh":input(),"ball":input()}

with open("talabalar.txt","a") as f:
    f.write(f"{talaba['ism']} {talaba['yosh']} {talaba['ball']}\n")