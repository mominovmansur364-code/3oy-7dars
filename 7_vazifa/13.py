import json

ism = input()
yosh = int(input())
ball = int(input())

talaba = {"ism": ism, "yosh": yosh, "ball": ball}

with open("talaba.json", "w") as f:
  json.dump(talaba, f, indent=4)