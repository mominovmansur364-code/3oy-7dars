n = int(input())

avtomobillar = []

for i in range(n):
  qator = input().split()
  marka = qator[0]
  yil = qator[1]
  narxi = qator[2]

  avtomobil = {"marka": marka, "yil": yil, "narxi": narxi}
  avtomobillar.append(avtomobil)

with open("avtomobillar.txt", "a") as f:
  for m in avtomobillar:
    f.write(f"{m['marka']} {m['yil']} {m['narxi']}\n")