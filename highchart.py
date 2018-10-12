import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
months = []
nflx = []
aapl = []
dvmt = []
fb = []
msft = []

with open("stock-high-2018.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader:
        months.append(row[0])
        nflx.append(int(row[1]))
        aapl.append(int(row[2]))
        dvmt.append(int(row[3]))
        fb.append(int(row[4]))
        msft.append(int(row[5]))

plt.plot(months, nflx, color='#CE0404', marker='o', linestyle='solid', label='Netflix (NFLX)')
plt.plot(months, aapl, color='#0B8AFA', marker='o', linestyle='solid', label='Apple (AAPL)')
plt.plot(months, dvmt, color='#FBFB16', marker='o', linestyle='solid', label='Dell (DVMT)')
plt.plot(months, fb, color='#4EF4FF', marker='o', linestyle='solid', label='Facebook (FB)')
plt.plot(months, msft, color='#71FF4E', marker='o', linestyle='solid', label='Microsft (MSFT)')
plt.legend(loc='upper left')
plt.ylabel("High Price")
plt.xlabel("Date Range")
plt.xticks(rotation=45, ha="right")
plt.show()
