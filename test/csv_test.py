import csv

with open('test.csv', 'w+') as csvfile:
    numberwriter = csv.writer(csvfile)

    for item in range(100):
        numberwriter.writerow([item, item, item])



