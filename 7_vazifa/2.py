mahsulot = {"nomi": input(), "narxi": input(), "miqdori": input()}


with open("mahsulot.txt", "w") as f:
  f.write(f"{mahsulot['nomi']}\n")
  f.write(f"{mahsulot['narxi']}\n")
  f.write(f"{mahsulot['miqdori']}\n")