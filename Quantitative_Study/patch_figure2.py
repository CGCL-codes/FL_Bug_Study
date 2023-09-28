import seaborn as sns
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = ['Arial']

random.seed(1)
lines_list = list(np.arange(0, 300, 2))
DL_lines_dict = dict.fromkeys(lines_list, 0)
FL_lines_dict = dict.fromkeys(lines_list, 0)

DL_file = "DL_Patch.csv"
FL_file = "FL_Patch.csv"
DL_rate_list = []
FL_rate_list = []
for file in [DL_file, FL_file]:
    df = pd.read_csv(file, sep=",")
    total_list = df["total"].tolist() if file == DL_file else random.sample(df["total"].tolist(), 160)
    for i in range(len(total_list)):
        for lines in lines_list:
            if total_list[i] <= lines:
                if file == DL_file:
                    DL_lines_dict[lines] += 1
                else:
                    FL_lines_dict[lines] += 1

    sumBug = len(total_list)
    if file == DL_file:
        for lines in DL_lines_dict:
            DL_rate_list.append(DL_lines_dict[lines] / sumBug)
    else:
        for lines in FL_lines_dict:
            FL_rate_list.append(FL_lines_dict[lines] / sumBug)

plt.figure(figsize=(4, 3))
plt.plot(lines_list, DL_rate_list, label=u'DL', linewidth=1, color='#67AB9F', markersize=5, linestyle='dashed')
plt.plot(lines_list, FL_rate_list, label=u'FL', linewidth=1, color='black', markersize=5)

plt.tick_params(labelsize=15)
y = list(np.arange(0, 1.01, 0.25))
plt.yticks(y, ["0", "25%", "50%", "75%", "100%"])

plt.legend(loc='best',fontsize=13)
plt.show()
# plt.savefig('patch_figure_2.pdf', format='pdf', bbox_inches='tight')