n = int(input())

mahsulotlar = []

for i in range(n):
  qator = input().split()
  nomi = qator[0]
  narxi = qator[1]
  miqdori = qator[2]

  mahsulot = {"nomi": nomi, "narxi": narxi, "miqdori": miqdori}
  mahsulotlar.append(mahsulot)

with open("mahsulotlar.txt", "w") as f:
  for m in mahsulotlar:
    f.write(f"{m['nomi']} {m['narxi']} {m['miqdori']}\n")