n = int(input())

xodimlar = []

for i in range(n):
  qator = input().split()
  ism= qator[0]
  yosh = qator[1]
  oylik = qator[2]

  xodim = {"ism": ism, "yosh": yosh, "oylik": oylik}
  xodimlar.append(xodim)

with open("xodimlar.txt", "w") as f:
  for m in xodimlar:
    f.write(f"{m['ism']} {m['yosh']} {m['oylik']}\n")