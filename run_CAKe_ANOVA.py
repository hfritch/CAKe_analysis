import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pingouin as pg


def rm22_bar_graph(a1, a2, b1, b2, barwidth, grouplabels, condlabels):
    """
    Make a bar graph with significance indicators for a 2x2 repeated measures design (two groups, two conditions).
    :param a1: data for group 1, condition 1
    :param a2: data for group 1, condition 2
    :param b1: data for group 2, condition 1
    :param b2: data for group 2, condition 2
    :param barwidth: desired width of bars
    :param grouplabels: names of groups (for legend)
    :param condlabels: names of conditions (for x-ticks)
    """
    a = [a1.mean(), a2.mean()]
    a_sem = [stats.sem(a1), stats.sem(a2)]
    b = [b1.mean(), b2.mean()]
    b_sem = [stats.sem(b1), stats.sem(b2)]
    bar1 = np.arange(len(a))
    bar2 = [x + barwidth for x in bar1]
    # Make the plot
    plt.bar(bar1, a, yerr=a_sem, capsize=5, color='steelblue', width=barWidth, label=grouplabels[0])
    plt.bar(bar2, b, yerr=b_sem, capsize=5, color='lightsteelblue', width=barWidth, label=grouplabels[1])
    # Add xticks
    plt.xticks([r + barwidth/2 for r in range(len(bar1))], condlabels)
    plt.legend()
    # run t-tests and add significance lines if appropriate
    adata = [a1, a2]
    bdata = [b1, b2]
    for i in range(2):
        t, p = stats.ttest_ind(a=adata[i], b=bdata[i])
        if p < .05:
            if p >= .01:  # determine number of asterisks
                text = '*'
            elif .01 > p >= .001:
                text = '**'
            elif .001 > p:
                text = '***'
            x1 = bar1[i]  # x-value of first bar to compare
            x2 = bar2[i]  # x-value of second bar
            ys = np.array([a + b]) + 2*np.array([a_sem + b_sem])  # find out how high the bars + error markers go
            y1 = ys.max() + .05  # y-value of sig bar (placed above the height of max bar + sem)
            y2 = y1 - .01  # bottom of vertical tick
            plt.plot([x1, x1, x2, x2], [y2, y1, y1, y2], linewidth=1, color='k')
            plt.text((x1+x2)/2, y1+.01, text, ha='center')


if __name__ == '__main__':
    # load in data
    d = pd.read_csv('older_adult_data.csv')
    # rename columns so they are easier to work with
    d.rename(columns={'CAKe score': 'CAKe', 'context source accuracy': 'SourceAccC',
                      'feature source accuracy': 'SourceAccF', 'context item accuracy': 'ItemAccC',
                      'feature item accuracy': 'ItemAccF'}, inplace=True)

    # analysis of 'normal' and 'impaired' groups
    # restructure dataframe for ANOVA
    Ps = np.tile(np.arange(1, len(d)+1), 2)  # participant numbers
    Task = np.hstack((np.ones(len(d)), np.ones(len(d))*2))  # 1 = feature, 2 = context
    # organize memory accuracies by CAKe group and task
    Accs = np.hstack((d.loc[d["CAKe"] >= 21, "SourceAccF"], d.loc[d["CAKe"] < 21, "SourceAccF"],
                      d.loc[d["CAKe"] >= 21, "SourceAccC"], d.loc[d["CAKe"] < 21, "SourceAccC"]))
    # Find out how many participants in each group to make group variable
    nNormal = sum(d["CAKe"] >= 21)
    nImpaired = sum(d["CAKe"] < 21)
    Group = np.hstack((np.ones(nNormal), np.ones(nImpaired)*2, np.ones(nNormal), np.ones(nImpaired)*2))  # 1 = normal, 2 = impaired
    # put variables together in dataframe
    d2 = pd.DataFrame({'Ps': Ps, 'Task': Task, 'Accs': Accs, 'Group': Group})

    # Run the two-way mixed-design ANOVA
    aov = pg.mixed_anova(dv='Accs', within='Task', between='Group', subject='Ps', data=d2)
    pg.print_table(aov)

    # Make bar graph to illustrate results
    fig = plt.figure(2, figsize=(12, 6))
    barWidth = 0.2
    # plot source memory in subplot1
    ax1 = fig.add_subplot(1, 2, 1)
    # get source memory accuracies for 'normal' (CAKe >= 21) and 'impaired' (CAKe < 21) groups
    normalSourceF = d.loc[d["CAKe"] >= 21, "SourceAccF"]
    normalSourceC = d.loc[d["CAKe"] >= 21, "SourceAccF"]
    impairedSourceF = d.loc[d["CAKe"] < 21, "SourceAccF"]
    impairedSourceC = d.loc[d["CAKe"] < 21, "SourceAccC"]
    # make bar graph
    rm22_bar_graph(normalSourceF, normalSourceC, impairedSourceF, impairedSourceC, barWidth, ['Normal', 'Impaired'],
                   ['Feature', 'Context'])
    # set labels
    ax1.set_ylabel('Memory Accuracy', fontsize=15)
    ax1.set_title('Source Memory', fontweight='bold', fontsize=15)

    # plot item memory in subplot2
    ax2 = fig.add_subplot(1, 2, 2)
    # get item memory accuracies for 'normal' (CAKe >= 21) and 'impaired' (CAKe < 21) groups
    normalItemF = d.loc[d["CAKe"] >= 21, "ItemAccF"]
    normalItemC = d.loc[d["CAKe"] >= 21, "ItemAccC"]
    impairedItemF = d.loc[d["CAKe"] < 21, "ItemAccF"]
    impairedItemC = d.loc[d["CAKe"] < 21, "ItemAccC"]
    # make bar graph
    rm22_bar_graph(normalItemF, normalItemC, impairedItemF, impairedItemC, barWidth, ['Normal', 'Impaired'],
                   ['Feature', 'Context'])
    # set labels
    ax2.set_ylabel('Memory Accuracy', fontsize=15)
    ax2.set_title('Item Memory', fontweight='bold', fontsize=15)
    plt.show()
