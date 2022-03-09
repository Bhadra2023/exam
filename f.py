import csv
with open("dep.csv",newline='') as csvfile:
    f = csv.DictReader("csvfile")
    print(f)
print("name      period")
print("________________")
for i in f:
    print(i['name'],i['period'])

