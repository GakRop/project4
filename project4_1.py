import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import sklearn
import csv

car_data_BH_R_44 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_44')
car_data_BH_R_63 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_63')
car_data_BH_R_1 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_1')
car_data_BH_R_11 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_1')
car_data_BH_R_16 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_16')
car_data_BH_R_55 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_55')
car_data_BH_R_4 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_4')
car_data_BH_R_3 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_3')
car_data_BH_R_14 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_14')
car_data_BH_R_31 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_31')
car_data_BH_R_10 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_10')
car_data_BH_R_22 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_22')
car_data_BH_R_5 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_5')
car_data_BH_R_18 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_18')
car_data_BH_R_77 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_77')
car_data_BH_R_24 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_24')
car_data_BH_R_23 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_23')
car_data_BH_R_6 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_6')
car_data_BH_R_20 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_20')
car_data_BH_R_47 = pd.read_csv(r'D:\project4_data\BH\car_data_BH_R_47')

print(car_data_BH_R_44.loc[:,"Unnamed: 0"])

