import csv

dates=[]
price=[]
with open('GOOG.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} opening price is {row[1]}')
            line_count += 1
            dates.append(row[0])
            price.append(row[1])
    print(f'Processed {line_count} lines.')


print(dates)
print(price)

##calculate average open price 
sum=0
count=0
for p in price:
    sum+=float(p)
    count+=1
mean=sum/count
print(mean)

sum_sq = 0
for p in price:
    sum_sq += (count-1)
var=sum_sq/(count-1)
print(var)

##find the optimal buy/sell date
max=0
for b in range(len(price)-1):
    for s in range(b+1,len(price)):
         profit=float(price[s])-float(price[b])
         if profit > max:
             max = profit
print(max)


