import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#plt.style.use('_mpl-gallery')

headers = ["Month", "Amount"]
df = pd.read_csv('test1.csv', names=headers)
print("Contents in csv file:\n", df)

df.set_index('Month').plot()
#fig = plt.figure()  # an empty figure with no Axes
#fig, ax = plt.subplots()  # a figure with a single Axes
#fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
#plt.plot(df.Month, df.Amount)
#plt.plot(df['Month'], df['Amount'])
#plt.plot(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], [1, 2, 5, 4, 3, 6])

plt.ylabel('Amount')
plt.xlabel('Month')
plt.show()
