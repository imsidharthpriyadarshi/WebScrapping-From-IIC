import csv
fileds=["name", "designation", "email"]
writer=None
file = open('document.csv','a')
writer=csv.writer(file)
writer.writerow(fileds)

for i in range(100):
    fileds=[str(i), str(i+1),str(i+2)]
    writer.writerow(fileds)
        