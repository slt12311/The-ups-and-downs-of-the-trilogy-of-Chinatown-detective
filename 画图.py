
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def fiveNumber(nums):
    # 五数概括 Minimum（最小值）、Q1、Median（中位数、）、Q3、Maximum（最大值）
    Minimum = min(nums)
    Maximum = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)

    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR  # 下限值
    upper_limit = Q3 + 1.5 * IQR  # 上限值

    return Minimum, Q1, Median, Q3, Maximum, lower_limit, upper_limit


if __name__ == '__main__':
    def num_sum(text):
        if text == '' or text == 0:
            return 0
        text = str(text)
        items = text.split(' ')
        counters = {}
        for item in items:
            if item in counters:
                continue
            else:
                counters[item] = 1
        return len(counters)-1

    write = pd.ExcelWriter('情感评分表.xlsx')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    #数据清洗
    order = ['唐探1', '唐探2', '唐探3', '唐探1-b', '唐探2-b', '唐探3-b']
    for name in order:
        df_1 = pd.read_excel('情感分析.xlsx', name, usecols=[0, 1, 2],
                             names=['情感评分', '评论', '评分'])
        df_1.fillna(0, inplace=True)
        df_1['个数']= df_1['评论'].apply(num_sum)
        df_2 = df_1[(df_1['个数'] > 3)]
        df_2.to_excel(write, sheet_name=name, index=False)
    write.save()

    #数据读取
    plt.rcParams['axes.unicode_minus'] = False
    df_1 = pd.read_excel('情感分析表.xlsx', '唐探1', usecols=[0],
                         names=['评分'])
    df_1['名称'] = '唐探 1'
    print(fiveNumber(df_1['评分']))

    df_2 = pd.read_excel('情感分析表.xlsx', '唐探2', usecols=[0],
                         names=['评分'])
    df_2['名称'] = '唐探 2'
    print(fiveNumber(df_2['评分']))

    df_3 = pd.read_excel('情感分析表.xlsx', '唐探3', usecols=[0],
                         names=['评分'])
    df_3['名称'] = '唐探 3'
    print(fiveNumber(df_3['评分']))

    # 画图

    color1 = ['#ffafaf', '#f47086', '#0095d9']
    frames = [df_1, df_2, df_3]
    df = pd.concat(frames, ignore_index=True)
    # print(df.head())
    plt.figure(figsize=(13, 6.5))
    with sns.axes_style('darkgrid'):

        #箱型图
        sns.boxplot(x="名称", y="评分", hue="名称",
                data=df, palette=color1)
        sns.distplot(df_1['评分'], color=color1[0])

        # 直方图
        sns.distplot(df_1['评分'],hist=False,
                     hist_kws={'color': color1[0]},
                     kde_kws={"color": color1[0], "lw": 1.5},
                     label='唐探1')
        sns.distplot(df_2['评分'],hist=False,
                     # hist_kws={'color': color1[1]},
                     kde_kws={"color": color1[1], "lw": 1.5},
                     label='唐探2')
        sns.distplot(df_3['评分'],hist=False,
                     hist_kws={'color': color1[2]},
                     kde_kws={"color": color1[2], "lw": 1.5},
                     label='唐探3')
        # sns.distplot(df_3['评分'], color=color1[2])

    #直方图辅助线
    mean1 = df_1['评分'].mean()
    mean2 = df_2['评分'].mean()
    mean3 = df_3['评分'].mean()
    plt.axvline(mean1, color=color1[0], linestyle=":", alpha=0.8)
    plt.text(mean1 + 0.01, 0.015, '唐探1: %.1f' % (mean1), color=color1[0])
    plt.axvline(mean2, color=color1[1], linestyle=":", alpha=0.8)
    plt.text(mean2 + 0.01, 0.010, '唐探2: %.1f' % (mean2), color=color1[1])
    plt.axvline(mean3, color=color1[2], linestyle=":", alpha=0.8)
    plt.text(mean3 + 0.01, 0.02, '唐探3: %.1f' % (mean3), color=color1[2])
    # plt.show()


    #条形图

    pall = sns.color_palette([ '#ffafaf','#f47086', '#0095d9'])
    sns.set_palette(pall)
    df = pd.read_excel('评分.xlsx', 'Sheet1', usecols=[0,1,2],
                         names=['等级','占比','名称'])
    with sns.axes_style('darkgrid'):
        sns.barplot(x='等级', y='占比', hue='名称',data=df )
    for x, y, p in zip(df['等级'], df['占比'], df['名称']):
        # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
        if p == '唐探1':
            plt.text(x=x,  y=y + 0.1, s= y,
            color = color1[0])
        elif p =='唐探2':
            plt.text(x=x, y=y + 0.1, s=y,
                     color=color1[1])
        else:
            plt.text(x=x, y=y + 0.1, s=y,
                     color=color1[2])

    #图例
    num1 = 1.01
    num2 = 0
    num3 = 3
    num4 = 0
    leg = plt.legend(bbox_to_anchor=(num1, num2), loc=num3, borderaxespad=num4)
    axes = plt.gca()
    axes.set_xlim([-25, 25])
    leg.get_frame().set_linewidth(0.0)

    plt.show()
