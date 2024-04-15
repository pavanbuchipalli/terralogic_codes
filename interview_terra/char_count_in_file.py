with open("CSV.data", "r+") as f1:
    data = f1.readlines()
for i in data:
    print(i.count("a"))