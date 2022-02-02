import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
ch_d2 = pd.read_csv("Chilla_data2_for_plots.csv")

my_pal = {'Employed':'g', 'Unemplyed':'r', 'Student':'b'}
# Prepare FacetGrid data
obj = sns.FacetGrid(ch_d2, col='Qualification', row='Where_you_live?',
                    sharey=False, sharex=False)
obj.map_dataframe(sns.scatterplot, x='age', y='daily_coding_time',
                    hue="What_are_you?", palette=my_pal)
obj.set_titles(col_template='{col_name}', row_template='{row_name}')
obj.add_legend()

#  Draw a plot
plt.show()