import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

headers = ["Month", "Amount"]
df1 = pd.read_csv('test1.csv', names=headers)
df2 = pd.read_csv('test2.csv', names=headers)
print("Contents in csv file:\n", df1, df2)

# plot
#df.set_index('Month').plot()
#plt.plot(df.Month, df.Amount)
#plt.plot(df['Month'], df['Amount'])
#fig = plt.figure()
fig, ax = plt.subplots()
#ax.plot(df1.Month, df1.Amount, label='2021')
#ax.plot(df2.Month, df2.Amount, label='2022')
ax.scatter(df1.Month, df1.Amount, label='Y 2021')
ax.scatter(df2.Month, df2.Amount, label='Y 2022')


#plt.ylabel('Amount')
#plt.xlabel('Month')
#plt.title('Sales')
#plt.legend();
ax.set_xlabel('Month')  # Add an x-label to the axes.
ax.set_ylabel('Amount')  # Add a y-label to the axes.
ax.set_title("Sales")  # Add a title to the axes.
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis(['Jan', 'Dec', 0, 15000])
ax.legend();  # Add a legend.
ax.grid(True);
plt.show()
