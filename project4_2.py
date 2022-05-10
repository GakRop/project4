import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import math
import statistics
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from statistics import mean

label_according_to_team = ["#00D2BE", "#00D2BE", "#0600EF", "#0600EF",
                           "#DC0000", "#DC0000", "#FF8700", "#FF8700",
                           "#0090FF", "#0090FF", "#2B4562", "#2B4562",
                           "#006F62", "#006F62", "#900000", "#900000",
                           "#005AFF", "#005AFF", "#FFFFFF", "#FFFFFF"]

label_according_to_PU = ["#00D2BE", "#00D2BE", "#0600EF", "#0600EF",
                           "#DC0000", "#DC0000", "#00D2BE", "#00D2BE",
                           "#0090FF", "#0090FF", "#0600EF", "#0600EF",
                           "#00D2BE", "#00D2BE", "#DC0000", "#DC0000",
                           "#00D2BE", "#00D2BE", "#DC0000", "#DC0000"]

marker = ["*", "^", "*", "^", "*", "^", "*", "^", "*", "^",
          "*", "^", "*", "^", "*", "^", "*", "^", "*", "^"]

result_R = [[3, 4, 19, 18, 1, 2, 14, 15, 9, 7, 20, 8, 17, 12, 6, 10, 13, 16, 5, 11],
            [10, 5, 1, 4, 2, 3, 7, 20, 20, 6, 8, 20, 12, 13, 20, 11, 14, 20, 9, 20],
            [4, 3, 20, 2, 1, 20, 5, 6, 17, 7, 9, 15, 20, 12, 8, 11, 10, 16, 14, 13]]

laptime_average_R = [[0 for i in range(20)] for j in range(3)]
fastest_lap_Q = [[0 for i in range(20)] for j in range(3)]

timing_data_BH_R_0 = [pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_44'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_63'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_1'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_11'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_16'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_55'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_4'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_3'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_14'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_31'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_10'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_22'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_5'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_18'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_77'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_24'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_23'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_6'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_20'),
                      pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_R_47')]

timing_data_SA_R_0 = [pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_44'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_63'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_1'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_11'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_16'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_55'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_4'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_3'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_14'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_31'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_10'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_22'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_5'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_18'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_77'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_24'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_23'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_6'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_20'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_R_47')]

timing_data_AU_R_0 = [pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_44'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_63'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_1'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_11'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_16'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_55'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_4'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_3'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_14'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_31'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_10'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_22'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_5'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_18'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_77'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_24'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_23'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_6'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_20'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_R_47')]

timing_data_R_0 = [timing_data_BH_R_0, timing_data_SA_R_0, timing_data_AU_R_0]

timing_data_BH_Q_0 = [pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_44'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_63'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_1'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_11'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_16'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_55'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_4'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_3'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_14'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_31'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_10'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_22'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_5'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_18'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_77'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_24'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_23'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_6'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_20'),
                    pd.read_csv(r'D:\project4_data\BH\timing_data_BH_0_Q_47')]

timing_data_SA_Q_0 = [pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_44'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_63'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_1'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_11'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_16'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_55'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_4'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_3'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_14'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_31'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_10'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_22'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_5'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_18'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_77'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_24'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_23'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_6'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_20'),
                      pd.read_csv(r'D:\project4_data\SA\timing_data_SA_0_Q_47')]

timing_data_AU_Q_0 = [pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_44'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_63'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_1'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_11'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_16'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_55'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_4'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_3'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_14'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_31'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_10'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_22'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_5'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_18'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_77'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_24'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_23'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_6'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_20'),
                      pd.read_csv(r'D:\project4_data\AU\timing_data_AU_0_Q_47')]

timing_data_Q_0 = [timing_data_BH_Q_0, timing_data_SA_Q_0, timing_data_AU_Q_0]

#SpeedMean contains the average speed
#SpeedMean = [SpeedMean of BH, SpeedMean of SA, SpeedMean of AU]
#SpeedMean of OO = [data of 20 drivers]
#data of each driver = [average of SpeedI1, SpeedI2, SpeedFL, SpeedST, average of all]

SpeedMean = [[[0 for i in range(5)] for j in range(20)] for k in range(3)]

df11 = pd.DataFrame(data= {'SpeedI1': [0],
                         'SpeedI2': [0],
                         'SpeedFL': [0],
                         'SpeedST': [0],
                         'LapTime': [0],
                         'NumberOfLaps': [0],
                         'Driver': [22]})

df19 = pd.DataFrame(data= {'SpeedI1': [0],
                         'SpeedI2': [0],
                         'SpeedFL': [0],
                         'SpeedST': [0],
                         'LapTime': [0],
                         'NumberOfLaps': [0],
                         'Driver': [47]})

timing_data_R_0[1][11] = df11
timing_data_R_0[1][19] = df19
timing_data_Q_0[1][2]['LapTime'][11] = float("NaN")
timing_data_Q_0[1][5]['LapTime'][11] = float("NaN")
#-----------------------------------------------------------------------------------------------------------------------
def speed_missing_value_filling():
    for i in range(len(timing_data_R_0)):
        for j in range(len(timing_data_R_0[i])):
            mean_of_SpeedI1 = timing_data_R_0[i][j]['SpeedI1'].mean()
            mean_of_SpeedI2 = timing_data_R_0[i][j]['SpeedI2'].mean()
            mean_of_SpeedFL = timing_data_R_0[i][j]['SpeedFL'].mean()
            mean_of_SpeedST = timing_data_R_0[i][j]['SpeedST'].mean()

            timing_data_R_0[i][j]['SpeedI1'].fillna(value = mean_of_SpeedI1, inplace=True)
            timing_data_R_0[i][j]['SpeedI2'].fillna(value = mean_of_SpeedI2, inplace=True)
            timing_data_R_0[i][j]['SpeedFL'].fillna(value = mean_of_SpeedFL, inplace=True)
            timing_data_R_0[i][j]['SpeedST'].fillna(value = mean_of_SpeedST, inplace=True)
            pass
#-----------------------------------------------------------------------------------------------------------------------
def laptime_missing_value_filling():
    for i in range(len(timing_data_R_0)):
        for j in range(len(timing_data_R_0[i])):
            mean_of_laptime = timing_data_R_0[i][j]['LapTime'].mean()

            timing_data_R_0[i][j]['LapTime'].fillna(value = mean_of_laptime, inplace=True)
#-----------------------------------------------------------------------------------------------------------------------
def Q_laptime_missing_value_filling():
    fill = 0.0
    fill = float(fill)
    for i in range(len(timing_data_Q_0)):
        for j in range(len(timing_data_Q_0[i])):
            timing_data_Q_0[i][j]['LapTime'].fillna(value = fill, inplace=True)
#-----------------------------------------------------------------------------------------------------------------------
def speed_average(list1, list2, list3, list4):
    list1 = list1.tolist()
    list2 = list2.tolist()
    list3 = list3.tolist()
    list4 = list4.tolist()
    sum1 = 0
    size1 = len(list1)
    sum2 = 0
    size2 = len(list2)
    sum3 = 0
    size3 = len(list3)
    sum4 = 0
    size4 = len(list4)

    for i in range (len(list1)):
        sum1 += list1[i]

    for i in range (len(list2)):
        sum2 += list2[i]

    for i in range (len(list3)):
        sum3 += list3[i]

    for i in range (len(list4)):
        sum4 += list4[i]

    mean_of_SpeedI1 = sum1/size1
    mean_of_SpeedI2 = sum2/size2
    mean_of_SpeedFL = sum3/size3
    mean_ofSpeedST = sum4/size4
    mean_of_all = math.fsum([sum1, sum2, sum3, sum4]) / sum([size1, size2, size3, size4])
    return mean_of_SpeedI1, mean_of_SpeedI2, mean_of_SpeedFL, mean_ofSpeedST, mean_of_all
#-----------------------------------------------------------------------------------------------------------------------
def speed_average_calling_function():
    for i in range(len(timing_data_R_0)):
        for j in range (len(timing_data_R_0[i])):
            mean_of_SpeedI1, mean_of_SpeedI2, mean_of_SpeedFL, mean_ofSpeedST, mean_of_all = speed_average(timing_data_R_0[i][j].loc[:, 'SpeedI1'],
                            timing_data_R_0[i][j].loc[:, "SpeedI2"],
                            timing_data_R_0[i][j].loc[:, "SpeedFL"],
                            timing_data_R_0[i][j].loc[:, "SpeedST"])

            SpeedMean[i][j][0] = mean_of_SpeedI1
            SpeedMean[i][j][1] = mean_of_SpeedI2
            SpeedMean[i][j][2] = mean_of_SpeedFL
            SpeedMean[i][j][3] = mean_ofSpeedST
            SpeedMean[i][j][4] = mean_of_all
    return
#-----------------------------------------------------------------------------------------------------------------------
def plot(x, y, title, label, x_lower, x_upper, y_lower, y_upper, xlabel, ylabel):
    plt.title(title)
    plt.scatter(x, y, color = label, edgecolors= "k")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xlim(x_lower, x_upper)
    plt.ylim(y_lower, y_upper)
    plt.savefig(title)
    plt.show()
#-----------------------------------------------------------------------------------------------------------------------
def plot_DBSCAN(x, y, title, label, x_lower, x_upper):
    D = np.array([[x[0], y[0]],
                  [x[1], y[1]],
                  [x[2], y[2]],
                  [x[3], y[3]],
                  [x[4], y[4]],
                  [x[5], y[5]],
                  [x[6], y[6]],
                  [x[7], y[7]],
                  [x[8], y[8]],
                  [x[9], y[9]],
                  [x[10], y[10]],
                  [x[11], y[11]],
                  [x[12], y[12]],
                  [x[13], y[13]],
                  [x[14], y[14]],
                  [x[15], y[15]],
                  [x[16], y[16]],
                  [x[17], y[17]],
                  [x[18], y[18]],
                  [x[19], y[19]],
    ])

    dbs = DBSCAN(eps = 3, min_samples=5)
    pred_labels = dbs.fit_predict(D)
    plt.title(title)
    plt.scatter(D[:,0], D[:,1], c= pred_labels)
    plt.xlabel("speed")
    plt.ylabel("result")
    plt.xlim(x_lower, x_upper)
    plt.ylim(20, 0)
    plt.savefig(title)
    plt.show()
#-----------------------------------------------------------------------------------------------------------------------
def laptime_plot_iterator():
    dict = {
        0: "Bahrain",
        1: "Saudi Arabia",
        2: "Australia"
    }

    xlimit = [[1, 57], [1,50], [1, 58]]
    ylimit = [[90, 155], [90, 155], [75, 155]]

    for i in range(len(timing_data_R_0)):
    #for i in range(1):
        for j in range(len(timing_data_R_0[i])):
        #for j in range(1):
            x = timing_data_R_0[i][j]['NumberOfLaps']
            y = timing_data_R_0[i][j]['LapTime']
            fig, ax = plt.subplots(figsize=(15,10))
            ax.set_facecolor('gray')
            ax.plot(x, y, c = label_according_to_team[j])
            plt.xlabel("Lap", fontsize = 20)
            plt.ylabel("Lap Time", fontsize = 20)
            ax.xaxis.set_major_locator(MultipleLocator(2))
            ax.yaxis.set_major_locator(MultipleLocator(2))
            plt.ylim(ylimit[i][0], ylimit[i][1])
            plt.xlim(xlimit[i][0], xlimit[i][1])
            ax.tick_params(axis='x', labelsize=17.5)
            ax.tick_params(axis='y', labelsize=15)
            title = str(timing_data_R_0[i][j]['Driver'][0])
            title = dict[i] + "_" + title
            plt.title(title, fontsize = 25)
            title = title+".png"
            plt.savefig(title, format="png")
            plt.show()
            print(title)
#-----------------------------------------------------------------------------------------------------------------------
def plot_race_laptime():
    xlimit = [[1, 57], [1, 50], [1, 58]]
    ylimit = [[90, 155], [90, 155], [75, 155]]

    for i in range(len(timing_data_R_0)):
        fig, ax = plt.subplots(figsize=(50,20))
        for j in range(len(timing_data_R_0[i])):
            x = timing_data_R_0[i][j]['NumberOfLaps']
            y = timing_data_R_0[i][j]['LapTime']
            ax.plot(x, y, c = label_according_to_team[j])
            plt.xlabel("Lap", fontsize = 30)
            plt.ylabel("Lap Time", fontsize = 30)
            plt.ylim(ylimit[i][0], ylimit[i][1])
            plt.xlim(xlimit[i][0], xlimit[i][1])
            ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.yaxis.set_major_locator(MultipleLocator(5))
            ax.tick_params(axis='x', labelsize=10)
            ax.tick_params(axis='y', labelsize=10)
            #title = str(timing_data_R_0[i][j]['Driver'][0])
            #title = dict[i] + " " + title

        title = dict[i]
        plt.title(title, fontsize = 60)
        fig.tight_layout()
        ax.set_facecolor('gray')
        plt.savefig(title)
        plt.show()
#-----------------------------------------------------------------------------------------------------------------------
def correlation(speed, result):
    correlation1 = statistics.correlation(speed[0], result)
    correlation2 = statistics.correlation(speed[1], result)
    correlation3 = statistics.correlation(speed[2], result)
    correlation4 = statistics.correlation(speed[3], result)

    return correlation1, correlation2, correlation3, correlation4
#-----------------------------------------------------------------------------------------------------------------------
def pca(title, w, x, y, z, C=4):
    D = np.array([[w[0], x[0], y[0], z[0]],
                  [w[1], x[1], y[1], z[1]],
                  [w[2], x[2], y[2], z[2]],
                  [w[3], x[3], y[3], z[3]],
                  [w[4], x[4], y[4], z[4]],
                  [w[5], x[5], y[5], z[5]],
                  [w[6], x[6], y[6], z[6]],
                  [w[7], x[7], y[7], z[7]],
                  [w[8], x[8], y[8], z[8]],
                  [w[9], x[9], y[9], z[9]],
                  [w[10], x[10], y[10], z[10]],
                  [w[11], x[11], y[11], z[11]],
                  [w[12], x[12], y[12], z[12]],
                  [w[13], x[13], y[13], z[13]],
                  [w[14], x[14], y[14], z[14]],
                  [w[15], x[15], y[15], z[15]],
                  [w[16], x[16], y[16], z[16]],
                  [w[17], x[17], y[17], z[17]],
                  [w[18], x[18], y[18], z[18]],
                  [w[19], x[19], y[19], z[19]],
                  ])

    multi_d_mean = np.mean(D, axis=0)
    centered_D = D - multi_d_mean
    pca = PCA(n_components=C)
    pca_transformed_D = pca.fit_transform(centered_D)

    for h in range(len(pca_transformed_D)):
        plt.scatter(pca_transformed_D[h][0], pca_transformed_D[h][1], s=100,
                    color=label_according_to_team[h], marker=marker[h], edgecolors= "k")
    plt.xlabel('PC0')
    plt.ylabel('PC1')
    plt.title(title)
    plt.savefig(title)
    plt.show()

    a = pca.explained_variance_ratio_
    b = []
    for i in range(len(a)):
        c = "{:.5f}".format(pca.explained_variance_ratio_[i])
        b.append(c)

    return b
#-----------------------------------------------------------------------------------------------------------------------
def convert_latptime(D):
    for i in range(len(D)):
        for j in range(len(D[i])):
            for k in range(len(D[i][j]['LapTime'])):
                if(type(D[i][j]['LapTime'][k]) == str):
                    l = D[i][j]['LapTime'][k]
                    time = []
                    a = float(l[8:9])
                    b = float(l[10:12])
                    c = float(l[13:23])
                    time.append(a)
                    time.append(b)
                    time.append(c)
                    t = a * 60 + b
                    t = t * 60 + c
                    t = round(t, 4)
                    D[i][j].at[k, 'LapTime'] = t
#-----------------------------------------------------------------------------------------------------------------------
def laptime_average(D):
    for i in range(len(D)):
        for j in range(len(D[i])):
            mean = D[i][j]['LapTime'].mean()
            laptime_average_R[i][j] = mean
#-----------------------------------------------------------------------------------------------------------------------
def fastest_lap(D):
    for i in range(len(D)):
        for j in range(len(D[i])):
            fastest = D[i][j]['LapTime'].min()
            fastest_lap_Q[i][j] = fastest
#-----------------------------------------------------------------------------------------------------------------------
def BH_stint_average():
    i = 0
    # 2-12, 16-29, 32-42, 45+52-53
    ver = timing_data_R_0[i][2]
    BH_R_1_laptime_stint1 = ver['LapTime'][1:12].mean()
    BH_R_1_laptime_stint2 = ver['LapTime'][15:29].mean()
    BH_R_1_laptime_stint3 = ver['LapTime'][31:43].mean()
    BH_R_1_laptime_stint4 = (ver['LapTime'][44] + ver['LapTime'][51:53].mean()) / 2
    average_1 = [BH_R_1_laptime_stint1, BH_R_1_laptime_stint2, BH_R_1_laptime_stint3, BH_R_1_laptime_stint4]

    # 2-14, 17-32, 35-42, 51-56
    per = timing_data_R_0[i][3]
    BH_R_11_laptime_stint1 = per['LapTime'][1:14].mean()
    BH_R_11_laptime_stint2 = per['LapTime'][16:32].mean()
    BH_R_11_laptime_stint3 = per['LapTime'][34:42].mean()
    BH_R_11_laptime_stint4 = per['LapTime'][50:56].mean()
    average_11 = [BH_R_11_laptime_stint1, BH_R_11_laptime_stint2, BH_R_11_laptime_stint3, BH_R_11_laptime_stint4]

    # 2-10, 13-26, 29-43, 51-57
    ham = timing_data_R_0[i][0]
    BH_R_44_laptime_stint1 = ham['LapTime'][1:11].mean()
    BH_R_44_laptime_stint2 = ham['LapTime'][12:26].mean()
    BH_R_44_laptime_stint3 = ham['LapTime'][28:43].mean()
    BH_R_44_laptime_stint4 = ham['LapTime'][50:57].mean()
    average_44 = [BH_R_44_laptime_stint1, BH_R_44_laptime_stint2, BH_R_44_laptime_stint3, BH_R_44_laptime_stint4]

    # 2-14, 17-32, 35-44, 51-57
    rus = timing_data_R_0[i][1]
    BH_R_63_laptime_stint1 = rus['LapTime'][1:14].mean()
    BH_R_63_laptime_stint2 = rus['LapTime'][16:32].mean()
    BH_R_63_laptime_stint3 = rus['LapTime'][34:44].mean()
    BH_R_63_laptime_stint4 = rus['LapTime'][50:57].mean()
    average_63 = [BH_R_63_laptime_stint1, BH_R_63_laptime_stint2, BH_R_63_laptime_stint3, BH_R_63_laptime_stint4]

    # 2-14, 17-30, 31-45, 51-57
    lec = timing_data_R_0[i][4]
    BH_R_16_laptime_stint1 = lec['LapTime'][1:14].mean()
    BH_R_16_laptime_stint2 = lec['LapTime'][16:30].mean()
    BH_R_16_laptime_stint3 = lec['LapTime'][30:45].mean()
    BH_R_16_laptime_stint4 = lec['LapTime'][50:57].mean()
    average_16 = [BH_R_16_laptime_stint1, BH_R_16_laptime_stint2, BH_R_16_laptime_stint3, BH_R_16_laptime_stint4]

    # 2-13, 16-32, 35-43, 51-57
    sai = timing_data_R_0[i][5]
    BH_R_55_laptime_stint1 = sai['LapTime'][1:13].mean()
    BH_R_55_laptime_stint2 = sai['LapTime'][15:32].mean()
    BH_R_55_laptime_stint3 = sai['LapTime'][34:43].mean()
    BH_R_55_laptime_stint4 = sai['LapTime'][50:57].mean()
    average_55 = [BH_R_55_laptime_stint1, BH_R_55_laptime_stint2, BH_R_55_laptime_stint3, BH_R_55_laptime_stint4]

    average = [average_44, average_63, average_1, average_11, average_16, average_55]
    return average
#-----------------------------------------------------------------------------------------------------------------------
def SA_stint_average():
    i = 1
    # 2-15, 21-37, 41-50
    ver = timing_data_R_0[i][2]
    BH_R_1_laptime_stint1 = ver['LapTime'][1:15].mean()
    BH_R_1_laptime_stint2 = (ver['LapTime'][21:37].mean()+ver['LapTime'][41:50].mean()) / 2
    average_1 = [BH_R_1_laptime_stint1, BH_R_1_laptime_stint2]

    # 2-14, 21-37, 42-50
    per = timing_data_R_0[i][3]
    BH_R_11_laptime_stint1 = per['LapTime'][1:14].mean()
    BH_R_11_laptime_stint2 = (per['LapTime'][20:37].mean()+per['LapTime'][40:50].mean()) / 2
    average_11 = [BH_R_11_laptime_stint1, BH_R_11_laptime_stint2]

    # 2-15, 21-36, 42-50
    ham = timing_data_R_0[i][0]
    BH_R_44_laptime_stint1 = (ham['LapTime'][1:15].mean() + ham['LapTime'][20:36].mean()) / 2
    BH_R_44_laptime_stint2 = ham['LapTime'][41:50].mean()
    average_44 = [BH_R_44_laptime_stint1, BH_R_44_laptime_stint2]

    # 2-15, 21-37, 41-50
    rus = timing_data_R_0[i][1]
    BH_R_63_laptime_stint1 = rus['LapTime'][1:15].mean()
    BH_R_63_laptime_stint2 = (rus['LapTime'][20:37].mean() + rus['LapTime'][40:50].mean()) / 2
    average_63 = [BH_R_63_laptime_stint1, BH_R_63_laptime_stint2]

    # 2-15, 21-37, 42-50
    lec = timing_data_R_0[i][4]
    BH_R_16_laptime_stint1 = lec['LapTime'][1:15].mean()
    BH_R_16_laptime_stint2 = (lec['LapTime'][20:37].mean() + lec['LapTime'][40:50].mean()) / 2
    average_16 = [BH_R_16_laptime_stint1, BH_R_16_laptime_stint2]

    # 2-15, 21-37, 42-50
    sai = timing_data_R_0[i][5]
    BH_R_55_laptime_stint1 = sai['LapTime'][1:15].mean()
    BH_R_55_laptime_stint2 = (sai['LapTime'][20:37].mean() + sai['LapTime'][40:50].mean()) / 2
    average_55 = [BH_R_55_laptime_stint1, BH_R_55_laptime_stint2]

    average = [average_44, average_63, average_1, average_11, average_16, average_55]
    return average
#-----------------------------------------------------------------------------------------------------------------------
def AU_stint_average():
    i = 2
    # 2, 7-17, 20-22, 28-38
    ver = timing_data_R_0[i][2]
    BH_R_1_laptime_stint1 = (ver['LapTime'][1] + ver['LapTime'][6:17].mean()) / 2
    BH_R_1_laptime_stint2 = (ver['LapTime'][19:22].mean() + ver['LapTime'][25:38].mean()) / 2
    average_1 = [BH_R_1_laptime_stint1, BH_R_1_laptime_stint2]

    # 2, 7-19, 22, 27-38, 41-58
    per = timing_data_R_0[i][3]
    BH_R_11_laptime_stint1 = (per['LapTime'][1] + per['LapTime'][6:19].mean()) / 2
    BH_R_11_laptime_stint2 = (per['LapTime'][21].mean() + per['LapTime'][26:38].mean() + per['LapTime'][40:58].mean()) / 3
    average_11 = [BH_R_11_laptime_stint1, BH_R_11_laptime_stint2]

    # 2, 7-21, 27-38, 41-58
    ham = timing_data_R_0[i][0]
    BH_R_44_laptime_stint1 = (ham['LapTime'][1] + ham['LapTime'][6:21].mean()) / 2
    BH_R_44_laptime_stint2 = (ham['LapTime'][24:38].mean() + ham['LapTime'][40:58].mean()) / 2
    average_44 = [BH_R_44_laptime_stint1, BH_R_44_laptime_stint2]

    # 2, 7-22, 27-38, 41-58
    rus = timing_data_R_0[i][1]
    BH_R_63_laptime_stint1 = (rus['LapTime'][1] + rus['LapTime'][6:22].mean()) / 2
    BH_R_63_laptime_stint2 = (rus['LapTime'][24:38].mean() + rus['LapTime'][40:58].mean()) / 2
    average_63 = [BH_R_63_laptime_stint1, BH_R_63_laptime_stint2]

    # 2, 7-21, 27-38, 41-58
    lec = timing_data_R_0[i][4]
    BH_R_16_laptime_stint1 = (lec['LapTime'][1] + lec['LapTime'][6:21].mean()) / 2
    BH_R_16_laptime_stint2 = (lec['LapTime'][24:38].mean() + lec['LapTime'][40:58].mean()) / 2
    average_16 = [BH_R_16_laptime_stint1, BH_R_16_laptime_stint2]

    #
    sai = timing_data_R_0[i][5]
    average_55 = "retired at 1st lap"

    average = [average_44, average_63, average_1, average_11, average_16, average_55]
    return average
#-----------------------------------------------------------------------------------------------------------------------
def main():
    #speed_missing_value_filling()
    #speed_average_calling_function()

    SpeedAll = [[0 for i in range(20)]for j in range(3)]
    SpeedI1 = [[0 for i in range(20)]for j in range(3)]
    SpeedI2 = [[0 for i in range(20)]for j in range(3)]
    SpeedFL = [[0 for i in range(20)]for j in range(3)]
    SpeedST = [[0 for i in range(20)]for j in range(3)]

    for i in range(len(SpeedMean)):
        for j in range(len(SpeedMean[i])):
            SpeedI1[i][j] = SpeedMean[i][j][0]
            SpeedI2[i][j] = SpeedMean[i][j][1]
            SpeedFL[i][j] = SpeedMean[i][j][2]
            SpeedST[i][j] = SpeedMean[i][j][3]
            SpeedAll[i][j] = SpeedMean[i][j][4]

    #plot(SpeedAll[0], result_R[0], "Bahrain GP speed vs result according to team",
    #                 label_according_to_team, 250, 265)
    #plot(SpeedAll[1], result_R[1], "Saudi Arabian GP speed vs result according to team",
    #                  label_according_to_team, 275, 290)
    #plot(SpeedAll[2], result_R[2], "Australian GP speed vs result according to team",
    #                  label_according_to_team, 265, 280)

    #plot(SpeedAll[0], result_R[0], "Bahrain GP speed vs result according to PU",
    #                  label_according_to_PU, 250, 265)
    #plot(SpeedAll[1], result_R[1], "Saudi Arabian GP speed vs result according to PU",
    #                  label_according_to_PU, 275, 290)
    #plot(SpeedAll[2], result_R[2], "Australian GP speed vs result according to PU",
    #                  label_according_to_PU, 265, 280)

    result_BH = []
    result_SA = []
    result_AU = []

    SpeedI1_BH = []
    SpeedI2_BH = []
    SpeedFL_BH = []
    SpeedST_BH = []

    SpeedI1_SA = []
    SpeedI2_SA = []
    SpeedFL_SA = []
    SpeedST_SA = []

    SpeedI1_AU = []
    SpeedI2_AU = []
    SpeedFL_AU = []
    SpeedST_AU = []

    for i in range (len(result_R[0])):
        if (result_R[0][i] != 20):
            result_BH.append(result_R[0][i])
            SpeedI1_BH.append(SpeedI1[0][i])
            SpeedI2_BH.append(SpeedI2[0][i])
            SpeedFL_BH.append(SpeedFL[0][i])
            SpeedST_BH.append(SpeedST[0][i])

    for i in range (len(result_R[1])):
        if (result_R[1][i] != 20):
            result_SA.append(result_R[1][i])
            SpeedI1_SA.append(SpeedI1[1][i])
            SpeedI2_SA.append(SpeedI2[1][i])
            SpeedFL_SA.append(SpeedFL[1][i])
            SpeedST_SA.append(SpeedST[1][i])

    for i in range (len(result_R[2])):
        if (result_R[2][i] != 20):
            result_AU.append(result_R[2][i])
            SpeedI1_AU.append(SpeedI1[2][i])
            SpeedI2_AU.append(SpeedI2[2][i])
            SpeedFL_AU.append(SpeedFL[2][i])
            SpeedST_AU.append(SpeedST[2][i])

    result_without_retire = [result_BH, result_SA, result_AU]
    BH = [SpeedI1_BH, SpeedI2_BH, SpeedFL_BH, SpeedST_BH]
    SA = [SpeedI1_SA, SpeedI2_SA, SpeedFL_SA, SpeedST_SA]
    AU = [SpeedI1_AU, SpeedI2_AU, SpeedFL_AU, SpeedST_AU]
    speed_without_retire = [BH, SA, AU]

    #correlation part
        #for i in range(len(result_without_retire)):
            #correlation1, correlation2, correlation3, correlation4 = \
                #correlation(speed_without_retire[i], result_without_retire[i])
            #print(correlation1)
            #print(correlation2)
            #print(correlation3)
            #print(correlation4)

        #for i in range(3):
            #w = []
            #x = []
            #y = []
            #z = []

            #dict = {
                #0: "BH PCA for SpeedI1, SpeedI2, SpeedFL, and SpeedST (team color+shape changed)",
                #1: "SA PCA for SpeedI1, SpeedI2, SpeedFL, and SpeedST (team color+shape changed)",
                #2: "AU PCA for SpeedI1, SpeedI2, SpeedFL, and SpeedST (team color+shape changed)",}

            #for j in range(20):
                #w.append(SpeedMean[i][j][0])
                #x.append(SpeedMean[i][j][1])
                #y.append(SpeedMean[i][j][2])
                #z.append(SpeedMean[i][j][3])

            #b = pca(dict[i], w, x, y, z)

        #for i in range(3):
            #D = []
            #for j in range(20):
                #D[j] = SpeedMean[i][j][0]
                #D[j] = SpeedMean[i][j][1]
                #D[j] = SpeedMean[i][j][2]
                #D[j] = SpeedMean[i][j][3]

            ##a = pca(D)

    convert_latptime(timing_data_R_0)
    laptime_missing_value_filling()
    laptime_average(timing_data_R_0)
    #plot(laptime_average_R[0], result_R[0], "Bahrain GP lap time vs result according to team",
    #                 label_according_to_team, 100, 105, "Lap Time", "Result")
    #plot(laptime_average_R[1], result_R[1], "Saudi Arabian GP lap time vs result according to team",
    #                  label_according_to_team, 95, 105, "Lap Time", "Result")
    #plot(laptime_average_R[2], result_R[2], "Australian GP lap time vs result according to team",
    #                  label_according_to_team, 85, 95, "Lap Time", "Result")

    convert_latptime(timing_data_Q_0)
    fastest_lap(timing_data_Q_0)

    #plot(fastest_lap_Q[0], laptime_average_R[0], "Bahrain GP Q fastest vs result according to team",
    #                 label_according_to_team, 95, 90, 105, 100, "Quali", "Race pace")
    #plot(fastest_lap_Q[1], laptime_average_R[1], "Saudi Arabian GP Q fastest vs result according to team",
    #                  label_according_to_team, 95, 85, 105, 95, "Quali", "Race pace")
    #plot(fastest_lap_Q[2], laptime_average_R[2], "Australian GP Q fastest vs result according to team",
    #                  label_according_to_team, 110, 75, 95, 85, "Quali", "Race pace")
    #plot(fastest_lap_Q[2], laptime_average_R[2], "Australian GP Q fastest vs result according to team without outlier",
    #                  label_according_to_team, 85, 75, 95, 85, "Quali", "Race pace")

    #laptime_plot_iterator()
    #plot_race_laptime

    average_1 = BH_stint_average()
    average_2 = SA_stint_average()
    average_3 = AU_stint_average()
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()