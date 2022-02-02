import seaborn as sns
import matplotlib.pyplot as plt
from numpy import median
import pandas as pd

# Load dataset
ch_d2 = pd.read_csv("Chilla_data2_for_plots.csv")

my_pal = {'Masters':'#ff0000', 'Bachelors':'#00ff00', 'PhD':'#0000ff', 'Pre-Bachelors':'#ffff00'}

#  Draw a line plot
sns.barplot(y="age", x="What_are_you?", hue="Qualification", palette=my_pal, data=ch_d2)
plt.show()