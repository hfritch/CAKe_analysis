import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def add_corr_line(x, y, color, style, label):
    """
    Calculate correlation between two variables and plot line of best fit.
    :param x: variable 1
    :param y: variable 2
    :param color: desired color of line
    :param style: desired line style
    :param label: label for legend (legend will say "{label}: r = _, p = _")
    """
    r, p = stats.pearsonr(x, y)  # calculate r and p
    a, b = np.polyfit(x, y, 1)  # find line of best fit
    # create label with r and significance level
    if p >= .05:
        text = f"{label}: r = {r:.2f}, p = {p:.2f}"
    elif .05 > p >= .01:
        text = f"{label}: r = {r:.2f}, p < .05"
    elif .01 > p >= .001:
        text = f"{label}: r = {r:.2f}, p < .01"
    elif p < .001:
        text = f"{label}: r = {r:.2f}, p < .001"
    # plot the line
    plt.plot(pd.Series(range(min(x), max(x) + 1)), a * pd.Series(range(min(x), max(x) + 1)) + b, color=color,
             linestyle=style, label=text)
    plt.legend(loc='upper right', fontsize=8)


if __name__ == '__main__':
    # load in data
    d = pd.read_csv('older_adult_data.csv')
    # rename columns so they are easier to work with
    d.rename(columns={'CAKe score': 'CAKe', 'context source accuracy': 'SourceAccC',
                      'feature source accuracy': 'SourceAccF', 'context item accuracy': 'ItemAccC',
                      'feature item accuracy': 'ItemAccF'}, inplace=True)
    d['Sex'] = d['Sex'].astype('category')

    # make correlation plot between CAKe scores and memory accuracy
    add_corr_line(d['CAKe'], d['SourceAccC'], 'royalblue', '-', 'Source memory(context)')
    add_corr_line(d['CAKe'], d['SourceAccF'], 'lightgreen', '-', 'Source memory(feature)')
    add_corr_line(d['CAKe'], d['ItemAccC'], 'royalblue', '--', 'Item memory(context)')
    add_corr_line(d['CAKe'], d['ItemAccF'], 'lightgreen', '--', 'Item memory(feature)')
    plt.xlabel('CAKe score', fontsize=15)
    plt.ylabel('Memory Accuracy', fontsize=15)
    plt.axis([24, 6, 0.7, 1])
    plt.show()

    # make correlation plot between CAKe scores and memory accuracy separated by sex
    fig = plt.figure(2, figsize=(12, 6))
    # plot female data in first subplot
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlabel('CAKe score', fontsize=15)
    ax1.set_ylabel('Memory Accuracy', fontsize=15)
    ax1.set_title('Females', fontweight='bold', fontsize=15)
    ax1.axis([24, 6, 0.7, 1])
    add_corr_line(d.loc[d["Sex"] == "Female", "CAKe"], d.loc[d["Sex"] == "Female", "SourceAccC"], 'royalblue', '-',
                  'Source memory(context)')
    add_corr_line(d.loc[d["Sex"] == "Female", "CAKe"], d.loc[d["Sex"] == "Female", "SourceAccF"], 'lightgreen', '-',
                  'Source memory(feature)')
    add_corr_line(d.loc[d["Sex"] == "Female", "CAKe"], d.loc[d["Sex"] == "Female", "ItemAccC"], 'royalblue', '--',
                  'Item memory(context)')
    add_corr_line(d.loc[d["Sex"] == "Female", "CAKe"], d.loc[d["Sex"] == "Female", "ItemAccF"], 'lightgreen', '--',
                  'Item memory(feature)')

    # add male data in second subplot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_xlabel('CAKe score', fontsize=15)
    ax2.set_ylabel('Memory Accuracy', fontsize=15)
    ax2.set_title('Males', fontweight='bold', fontsize=15)
    ax2.axis([24, 6, 0.7, 1])
    add_corr_line(d.loc[d["Sex"] == "Male", "CAKe"], d.loc[d["Sex"] == "Male", "SourceAccC"], 'royalblue', '-',
                  'Source memory(context)')
    add_corr_line(d.loc[d["Sex"] == "Male", "CAKe"], d.loc[d["Sex"] == "Male", "SourceAccF"], 'lightgreen', '-',
                  'Source memory(feature)')
    add_corr_line(d.loc[d["Sex"] == "Male", "CAKe"], d.loc[d["Sex"] == "Male", "ItemAccC"], 'royalblue', '--',
                  'Item memory(context)')
    add_corr_line(d.loc[d["Sex"] == "Male", "CAKe"], d.loc[d["Sex"] == "Male", "ItemAccF"], 'lightgreen', '--',
                  'Item memory(feature)')
    plt.show()
