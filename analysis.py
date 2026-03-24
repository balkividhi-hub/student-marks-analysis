import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("marks.csv")

# -------------------------------
# 1. Average marks per subject
# -------------------------------
avg_subject = df.groupby("Subject")["Marks"].mean()

plt.figure()
plt.pie(avg_subject, labels=avg_subject.index, autopct='%1.1f%%')
plt.title("Average Marks by Subject")
plt.show()

# -------------------------------
# 2. Filter Riya data
# -------------------------------
riya = df[df["Name"] == "Riya"]

plt.figure()
plt.pie(riya["Marks"], labels=riya["Subject"], autopct='%1.1f%%')
plt.title("Riya Marks Distribution")
plt.show()

# -------------------------------
# 3. Compare students (BAR GRAPH)
# -------------------------------
avg_student = df.groupby("Name")["Marks"].mean()

plt.figure()
plt.bar(avg_student.index, avg_student)
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
