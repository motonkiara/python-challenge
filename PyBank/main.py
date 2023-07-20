import csv
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    months = []
    profit_losses = []
    changes = []

    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

total_months = len(months)

net_total = sum(profit_losses)

for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

average_change = sum(changes) / len(changes)

greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

print('Financial Analysis')
print('-------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')
