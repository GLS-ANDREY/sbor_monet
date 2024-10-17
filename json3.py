import json
azvm = [
    ["Андрей", "Жуков","13"],
    ["Вячеслав","Матва","38"]
    ]
json2 = open("json2.txt", "w+")
json.dump(azvm,json2,indent=3)
json2.close()

