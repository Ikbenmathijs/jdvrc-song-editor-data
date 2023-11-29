import os
import json

path = "Images/GameIcons"
icons = os.listdir(path)

outp = []

for icon in icons:
    inp = input(f"game name for {icon}: ")


    outp.append({"id": icon[:-4], "name": inp, "filename": icon})

f = open("Data.json", "r", encoding="utf-8")
data = json.load(f)
f.close()

data["icons"] = outp

f = open("Data.json", "w", encoding="utf-8")
json.dump(data, f, indent=4)
f.close()
