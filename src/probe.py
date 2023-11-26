import csv

with open("items.csv", newline='', encoding='utf-8') as csvfile:
    print(csvfile)
    reader_1 = csv.reader(csvfile)
    skip_first = True
    for row in reader_1:
        if skip_first:
            skip_first = False
            continue
        name = row[0]
        price = row[1]
        quantity = row[2]
        print(name)
        print(price)
        print(quantity)
