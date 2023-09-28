import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import json
from statannot import add_stat_annotation
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Arial']

FL_changed_files_list = []
FL_functions_list = []
FL_hunks_list = []
DL_changed_files_list = []
DL_functions_list = []
DL_hunks_list = []

plt.figure(figsize=(3.4, 3))
dataSources = ['FL', 'DL']
for dataSource in dataSources:
    if dataSource == 'FL':
        data_file = "FL_Patch.csv"
        df = pd.read_csv(data_file, sep=",")
        FL_changed_files_list = random.sample(df["changed_files"].tolist(), 160)
        FL_functions_list = random.sample([eval(x)['num'] for x in df["functions"].tolist()], 160)
        FL_hunks_list = random.sample(df["hunks"].tolist(), 160)
    elif dataSource == 'DL':
        data_file = "DL_Patch.csv"
        df = pd.read_csv(data_file, sep=",")
        DL_changed_files_list = random.sample(df["changed_files"].tolist(), 160)
        DL_functions_list = random.sample([eval(x)['num'] for x in df["functions"].tolist()], 160)
        DL_hunks_list = random.sample(df["hunks"].tolist(), 160)

print(len(FL_changed_files_list),len(DL_changed_files_list),len(FL_functions_list),len(DL_functions_list))
sunBug = len(FL_changed_files_list)

type_list = []
for i in range(sunBug * 6):
    if i < sunBug * 3:
        type_list.append("DL")
    else:
        type_list.append("FL")

way_list = []
for i in range(sunBug * 6):
    if i < sunBug:
        way_list.append("Files")
    elif i < sunBug * 2:
        way_list.append("Functions")
    elif i < sunBug * 3:
        way_list.append("Hunks")
    elif i < sunBug * 4:
        way_list.append("Files")
    elif i < sunBug * 5:
        way_list.append("Functions")
    else:
        way_list.append("Hunks")

data = pd.DataFrame({
    "Values": DL_changed_files_list + DL_functions_list + DL_hunks_list + FL_changed_files_list + FL_functions_list + FL_hunks_list,
    "Source": type_list,
    "Way": way_list,
})

g = sns.boxplot(x='Way', y='Values', hue='Source', data=data, width=0.5, showfliers=False,
                palette=['#67AB9F', 'lightgray'])

add_stat_annotation(g, data=data, x='Way', y='Values', hue='Source',
                    box_pairs=[(("Files", "FL"), ("Files", "DL")),
                               (("Functions", "FL"), ("Functions", "DL")),
                                (("Hunks", "FL"), ("Hunks", "DL"))],
                    test='Mann-Whitney-gt', text_format='simple', loc='outside', comparisons_correction=None,
                    line_offset_to_box=4, line_offset=0.02, line_height=0.02, text_offset=5,
                    verbose=1,fontsize='large')
g.legend(loc="upper left")
plt.tick_params(labelsize=13)
g.set(xlabel=None, ylabel=None)
plt.tight_layout()
plt.show()
# plt.savefig('patch_figure_3.pdf', format='pdf', bbox_inches='tight')