mahsulot={"nomi":input(),"narxi":input(),"miqdori":input()}

with open("mahsulotlar.txt","a") as f:
    f.write(f"{mahsulot['nomi']} {mahsulot['narxi']} {mahsulot['miqdori']}\n")