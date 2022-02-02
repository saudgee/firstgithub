# import library
import pandas as pd

#import data from file
chilla = pd.read_csv("data_chilla.csv")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)

p= sns.countplot(x="Location", hue="Age",  data=chilla)
plt.show()