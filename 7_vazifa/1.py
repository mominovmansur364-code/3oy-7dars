talaba = {"ism": input(), "yosh": input(), "ball": input()}


with open("talaba.txt", "w") as f:
  f.write(f"{talaba['ism']}\n")
  f.write(f"{talaba['yosh']}\n")
  f.write(f"{talaba['ball']}\n")