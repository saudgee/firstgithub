# Steps Involved in Data Visualization

#  Step-1 Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step-2 Set the Theme
sns.set_theme(style="ticks", color_codes=True)

# Step-3 Import Dataset
titanic = sns.load_dataset("titanic")

# # Step-4 Plot basic graph with 1 variable
# p1 = sns.countplot(x="sex", data=titanic)
# p1.set_title("Plot for Counting")
# plt.show()

# Step-5 Plot basic graph with more than 1 variable
p1 = sns.countplot(x="sex", data=titanic, hue="class")
p1.set_title("Plot for Counting")
plt.show()