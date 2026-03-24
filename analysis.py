import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("marks.csv")

# Show first rows
print(df.head())

# Group data
avg = df.groupby("Subject")["Marks"].mean()
print(avg)

# Create pie chart
plt.pie(avg, labels=avg.index, autopct='%1.1f%%')
plt.title("Average Marks Distribution")

plt.show()