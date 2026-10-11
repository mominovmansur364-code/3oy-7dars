xodim = {"ism": input(), "yosh": input(), "oylik": input()}


with open("xodimlar.txt", "a") as f:
    f.write(f"{xodim['ism']} {xodim['yosh']} {xodim['oylik']}\n")