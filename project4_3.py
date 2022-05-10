import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import math
import statistics
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

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

timing_data_BH_R = [pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_44'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_63'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_1'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_11'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_16'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_55'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_4'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_3'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_14'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_31'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_10'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_22'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_5'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_18'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_77'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_24'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_23'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_6'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_20'),
                      pd.read_csv(r'D:\project4_data\BH\timing_app_data_BH_R_47')]

timing_data_SA_R = [pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_44'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_63'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_1'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_11'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_16'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_55'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_4'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_3'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_14'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_31'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_10'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_22'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_5'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_18'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_77'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_24'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_23'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_6'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_20'),
                      pd.read_csv(r'D:\project4_data\SA\timing_app_data_SA_R_47')]

timing_data_AU_R = [pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_44'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_63'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_1'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_11'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_16'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_55'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_4'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_3'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_14'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_31'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_10'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_22'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_5'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_18'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_77'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_24'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_23'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_6'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_20'),
                      pd.read_csv(r'D:\project4_data\AU\timing_app_data_AU_R_47')]

timing_data_R = [timing_data_BH_R, timing_data_SA_R, timing_data_AU_R]
#-----------------------------------------------------------------------------------------------------------------------
def main():
    print(timing_data_R[0][0].columns)
    print(timing_data_R[0][0]['Stint'])
    print(timing_data_R[0][0]['Compound'])

    for i in range(len(timing_data_R[0][0]['StartLaps'])):
        print(i, timing_data_R[0][0]['StartLaps'][i])

    print("done")
    return
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()