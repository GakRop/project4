import pandas as pd
import fastf1
#-----------------------------------------------------------------------------------------------------------------------
#timing_data_RaceName_index =
# [HAM, RUS, VER, PER, LEC, SAI, NOR, RIC, ALO, OCO,
# GAS, TSU, VET, STR, BOT, ZHO, ALB, LAT, MAG, MSC]
#-----------------------------------------------------------------------------------------------------------------------
car_data_BH = [[[] for i in range(5)]for j in range(20)]
car_data_SA = [[[] for i in range(5)]for j in range(20)]
car_data_AU = [[[] for i in range(5)]for j in range(20)]
#-----------------------------------------------------------------------------------------------------------------------
#importing the data for each session of all races
#the naming rule follow the rule below:
#the race code as the two-letter country code and the session
fastf1.Cache.enable_cache("C:\Python\project4")
BH_FP1 = fastf1.get_session(2022, 1, "FP1")
BH_FP2 = fastf1.get_session(2022, 1, "FP2")
BH_FP3 = fastf1.get_session(2022, 1, "FP3")
BH_Q = fastf1.get_session(2022, 1, "Q")
BH_R = fastf1.get_session(2022, 1, "R")
#-----------------------------------------------------------------------------------------------------------------------
SA_FP1 = fastf1.get_session(2022, 2, "FP1")
SA_FP2 = fastf1.get_session(2022, 2, "FP2")
SA_FP3 = fastf1.get_session(2022, 2, "FP3")
SA_Q = fastf1.get_session(2022, 2, "Q")
SA_R = fastf1.get_session(2022, 2, "R")
#-----------------------------------------------------------------------------------------------------------------------
AU_FP1 = fastf1.get_session(2022, 3, "FP1")
AU_FP2 = fastf1.get_session(2022, 3, "FP2")
AU_FP3 = fastf1.get_session(2022, 3, "FP3")
AU_Q = fastf1.get_session(2022, 3, "Q")
AU_R = fastf1.get_session(2022, 3, "R")
#-----------------------------------------------------------------------------------------------------------------------
car_data_BH_FP1 = fastf1.api.car_data(BH_FP1.api_path, response=None, livedata=None)
car_data_BH_FP2 = fastf1.api.car_data(BH_FP2.api_path, response=None, livedata=None)
car_data_BH_FP3 = fastf1.api.car_data(BH_FP3.api_path, response=None, livedata=None)
car_data_BH_Q = fastf1.api.car_data(BH_Q.api_path, response=None, livedata=None)
car_data_BH_R = fastf1.api.car_data(BH_R.api_path, response=None, livedata=None)
#-----------------------------------------------------------------------------------------------------------------------
car_data_SA_FP1 = fastf1.api.car_data(SA_FP1.api_path, response=None, livedata=None)
car_data_SA_FP2 = fastf1.api.car_data(SA_FP2.api_path, response=None, livedata=None)
car_data_SA_FP3 = fastf1.api.car_data(SA_FP3.api_path, response=None, livedata=None)
car_data_SA_Q = fastf1.api.car_data(SA_Q.api_path, response=None, livedata=None)
car_data_SA_R = fastf1.api.car_data(SA_R.api_path, response=None, livedata=None)
#-----------------------------------------------------------------------------------------------------------------------
car_data_AU_FP1 = fastf1.api.car_data(AU_FP1.api_path, response=None, livedata=None)
car_data_AU_FP2 = fastf1.api.car_data(AU_FP2.api_path, response=None, livedata=None)
car_data_AU_FP3 = fastf1.api.car_data(AU_FP3.api_path, response=None, livedata=None)
car_data_AU_Q = fastf1.api.car_data(AU_Q.api_path, response=None, livedata=None)
car_data_AU_R = fastf1.api.car_data(AU_R.api_path, response=None, livedata=None)
#-----------------------------------------------------------------------------------------------------------------------
def Car_data_BH():
    i = 0
    car_data_BH[0][i] = car_data_BH_FP1["44"]
    car_data_BH[1][i] = car_data_BH_FP1["63"]
    car_data_BH[2][i] = car_data_BH_FP1["1"]
    car_data_BH[3][i] = car_data_BH_FP1["11"]
    car_data_BH[4][i] = car_data_BH_FP1["16"]
    car_data_BH[5][i] = car_data_BH_FP1["55"]
    car_data_BH[6][i] = car_data_BH_FP1["3"]
    car_data_BH[7][i] = car_data_BH_FP1["4"]
    car_data_BH[8][i] = car_data_BH_FP1["14"]
    car_data_BH[9][i] = car_data_BH_FP1["31"]
    car_data_BH[10][i] = car_data_BH_FP1["10"]
    car_data_BH[11][i] = car_data_BH_FP1["22"]
    # car_data_BH[11][i] = car_data_BH_FP1["5"]
    car_data_BH[12][i] = car_data_BH_FP1["27"]
    car_data_BH[13][i] = car_data_BH_FP1["18"]
    car_data_BH[14][i] = car_data_BH_FP1["77"]
    car_data_BH[15][i] = car_data_BH_FP1["24"]
    car_data_BH[16][i] = car_data_BH_FP1["23"]
    car_data_BH[17][i] = car_data_BH_FP1["6"]
    car_data_BH[18][i] = car_data_BH_FP1["20"]
    car_data_BH[19][i] = car_data_BH_FP1["47"]

    i = 1
    car_data_BH[0][i] = car_data_BH_FP2["44"]
    car_data_BH[1][i] = car_data_BH_FP2["63"]
    car_data_BH[2][i] = car_data_BH_FP2["1"]
    car_data_BH[3][i] = car_data_BH_FP2["11"]
    car_data_BH[4][i] = car_data_BH_FP2["16"]
    car_data_BH[5][i] = car_data_BH_FP2["55"]
    car_data_BH[6][i] = car_data_BH_FP2["3"]
    car_data_BH[7][i] = car_data_BH_FP2["4"]
    car_data_BH[8][i] = car_data_BH_FP2["14"]
    car_data_BH[9][i] = car_data_BH_FP2["31"]
    car_data_BH[10][i] = car_data_BH_FP2["10"]
    car_data_BH[11][i] = car_data_BH_FP2["22"]
    #car_data_BH[11][i] = car_data_BH_FP2["5"]
    car_data_BH[12][i] = car_data_BH_FP2["27"]
    car_data_BH[13][i] = car_data_BH_FP2["18"]
    car_data_BH[14][i] = car_data_BH_FP2["77"]
    car_data_BH[15][i] = car_data_BH_FP2["24"]
    car_data_BH[16][i] = car_data_BH_FP2["23"]
    car_data_BH[17][i] = car_data_BH_FP2["6"]
    car_data_BH[18][i] = car_data_BH_FP2["20"]
    car_data_BH[19][i] = car_data_BH_FP2["47"]

    i = 2
    car_data_BH[0][i] = car_data_BH_FP3["44"]
    car_data_BH[1][i] = car_data_BH_FP3["63"]
    car_data_BH[2][i] = car_data_BH_FP3["1"]
    car_data_BH[3][i] = car_data_BH_FP3["11"]
    car_data_BH[4][i] = car_data_BH_FP3["16"]
    car_data_BH[5][i] = car_data_BH_FP3["55"]
    car_data_BH[6][i] = car_data_BH_FP3["3"]
    car_data_BH[7][i] = car_data_BH_FP3["4"]
    car_data_BH[8][i] = car_data_BH_FP3["14"]
    car_data_BH[9][i] = car_data_BH_FP3["31"]
    car_data_BH[10][i] = car_data_BH_FP3["10"]
    car_data_BH[11][i] = car_data_BH_FP3["22"]
    # car_data_BH[11][i] = car_data_BH_FP3["5"]
    car_data_BH[12][i] = car_data_BH_FP3["27"]
    car_data_BH[13][i] = car_data_BH_FP3["18"]
    car_data_BH[14][i] = car_data_BH_FP3["77"]
    car_data_BH[15][i] = car_data_BH_FP3["24"]
    car_data_BH[16][i] = car_data_BH_FP3["23"]
    car_data_BH[17][i] = car_data_BH_FP3["6"]
    car_data_BH[18][i] = car_data_BH_FP3["20"]
    car_data_BH[19][i] = car_data_BH_FP3["47"]

    i = 3
    car_data_BH[0][i] = car_data_BH_Q["44"]
    car_data_BH[1][i] = car_data_BH_Q["63"]
    car_data_BH[2][i] = car_data_BH_Q["1"]
    car_data_BH[3][i] = car_data_BH_Q["11"]
    car_data_BH[4][i] = car_data_BH_Q["16"]
    car_data_BH[5][i] = car_data_BH_Q["55"]
    car_data_BH[6][i] = car_data_BH_Q["3"]
    car_data_BH[7][i] = car_data_BH_Q["4"]
    car_data_BH[8][i] = car_data_BH_Q["14"]
    car_data_BH[9][i] = car_data_BH_Q["31"]
    car_data_BH[10][i] = car_data_BH_Q["10"]
    car_data_BH[11][i] = car_data_BH_Q["22"]
    # car_data_BH[11][i] = car_data_BH_Q["5"]
    car_data_BH[12][i] = car_data_BH_Q["27"]
    car_data_BH[13][i] = car_data_BH_Q["18"]
    car_data_BH[14][i] = car_data_BH_Q["77"]
    car_data_BH[15][i] = car_data_BH_Q["24"]
    car_data_BH[16][i] = car_data_BH_Q["23"]
    car_data_BH[17][i] = car_data_BH_Q["6"]
    car_data_BH[18][i] = car_data_BH_Q["20"]
    car_data_BH[19][i] = car_data_BH_Q["47"]

    i = 4
    car_data_BH[0][i] = car_data_BH_R["44"]
    car_data_BH[1][i] = car_data_BH_R["63"]
    car_data_BH[2][i] = car_data_BH_R["1"]
    car_data_BH[3][i] = car_data_BH_R["11"]
    car_data_BH[4][i] = car_data_BH_R["16"]
    car_data_BH[5][i] = car_data_BH_R["55"]
    car_data_BH[6][i] = car_data_BH_R["3"]
    car_data_BH[7][i] = car_data_BH_R["4"]
    car_data_BH[8][i] = car_data_BH_R["14"]
    car_data_BH[9][i] = car_data_BH_R["31"]
    car_data_BH[10][i] = car_data_BH_R["10"]
    car_data_BH[11][i] = car_data_BH_R["22"]
    # car_data_BH[11][i] = car_data_BH_R["5"]
    car_data_BH[12][i] = car_data_BH_R["27"]
    car_data_BH[13][i] = car_data_BH_R["18"]
    car_data_BH[14][i] = car_data_BH_R["77"]
    car_data_BH[15][i] = car_data_BH_R["24"]
    car_data_BH[16][i] = car_data_BH_R["23"]
    car_data_BH[17][i] = car_data_BH_R["6"]
    car_data_BH[18][i] = car_data_BH_R["20"]
    car_data_BH[19][i] = car_data_BH_R["47"]
    return

def Car_data_BH_Writer():
    i = 0
    car_data_BH[0][i].to_csv(r'car_data_BH_FP1_44')
    car_data_BH[1][i].to_csv(r'car_data_BH_FP1_63')
    car_data_BH[2][i].to_csv(r'car_data_BH_FP1_1')
    car_data_BH[3][i].to_csv(r'car_data_BH_FP1_11')
    car_data_BH[4][i].to_csv(r'car_data_BH_FP1_16')
    car_data_BH[5][i].to_csv(r'car_data_BH_FP1_55')
    car_data_BH[6][i].to_csv(r'car_data_BH_FP1_4')
    car_data_BH[7][i].to_csv(r'car_data_BH_FP1_3')
    car_data_BH[8][i].to_csv(r'car_data_BH_FP1_14')
    car_data_BH[9][i].to_csv(r'car_data_BH_FP1_31')
    car_data_BH[10][i].to_csv(r'car_data_BH_FP1_10')
    car_data_BH[11][i].to_csv(r'car_data_BH_FP1_22')
    car_data_BH[12][i].to_csv(r'car_data_BH_FP1_5')
    car_data_BH[13][i].to_csv(r'car_data_BH_FP1_18')
    car_data_BH[14][i].to_csv(r'car_data_BH_FP1_77')
    car_data_BH[15][i].to_csv(r'car_data_BH_FP1_24')
    car_data_BH[16][i].to_csv(r'car_data_BH_FP1_23')
    car_data_BH[17][i].to_csv(r'car_data_BH_FP1_6')
    car_data_BH[18][i].to_csv(r'car_data_BH_FP1_20')
    car_data_BH[19][i].to_csv(r'car_data_BH_FP1_47')

    i = 1
    car_data_BH[0][i].to_csv(r'car_data_BH_FP2_44')
    car_data_BH[1][i].to_csv(r'car_data_BH_FP2_63')
    car_data_BH[2][i].to_csv(r'car_data_BH_FP2_1')
    car_data_BH[3][i].to_csv(r'car_data_BH_FP2_11')
    car_data_BH[4][i].to_csv(r'car_data_BH_FP2_16')
    car_data_BH[5][i].to_csv(r'car_data_BH_FP2_55')
    car_data_BH[6][i].to_csv(r'car_data_BH_FP2_4')
    car_data_BH[7][i].to_csv(r'car_data_BH_FP2_3')
    car_data_BH[8][i].to_csv(r'car_data_BH_FP2_14')
    car_data_BH[9][i].to_csv(r'car_data_BH_FP2_31')
    car_data_BH[10][i].to_csv(r'car_data_BH_FP2_10')
    car_data_BH[11][i].to_csv(r'car_data_BH_FP2_22')
    car_data_BH[12][i].to_csv(r'car_data_BH_FP2_5')
    car_data_BH[13][i].to_csv(r'car_data_BH_FP2_18')
    car_data_BH[14][i].to_csv(r'car_data_BH_FP2_77')
    car_data_BH[15][i].to_csv(r'car_data_BH_FP2_24')
    car_data_BH[16][i].to_csv(r'car_data_BH_FP2_23')
    car_data_BH[17][i].to_csv(r'car_data_BH_FP2_6')
    car_data_BH[18][i].to_csv(r'car_data_BH_FP2_20')
    car_data_BH[19][i].to_csv(r'car_data_BH_FP2_47')

    i = 2
    car_data_BH[0][i].to_csv(r'car_data_BH_FP3_44')
    car_data_BH[1][i].to_csv(r'car_data_BH_FP3_63')
    car_data_BH[2][i].to_csv(r'car_data_BH_FP3_1')
    car_data_BH[3][i].to_csv(r'car_data_BH_FP3_11')
    car_data_BH[4][i].to_csv(r'car_data_BH_FP3_16')
    car_data_BH[5][i].to_csv(r'car_data_BH_FP3_55')
    car_data_BH[6][i].to_csv(r'car_data_BH_FP3_4')
    car_data_BH[7][i].to_csv(r'car_data_BH_FP3_3')
    car_data_BH[8][i].to_csv(r'car_data_BH_FP3_14')
    car_data_BH[9][i].to_csv(r'car_data_BH_FP3_31')
    car_data_BH[10][i].to_csv(r'car_data_BH_FP3_10')
    car_data_BH[11][i].to_csv(r'car_data_BH_FP3_22')
    car_data_BH[12][i].to_csv(r'car_data_BH_FP3_5')
    car_data_BH[13][i].to_csv(r'car_data_BH_FP3_18')
    car_data_BH[14][i].to_csv(r'car_data_BH_FP3_77')
    car_data_BH[15][i].to_csv(r'car_data_BH_FP3_24')
    car_data_BH[16][i].to_csv(r'car_data_BH_FP3_23')
    car_data_BH[17][i].to_csv(r'car_data_BH_FP3_6')
    car_data_BH[18][i].to_csv(r'car_data_BH_FP3_20')
    car_data_BH[19][i].to_csv(r'car_data_BH_FP3_47')

    i = 3
    car_data_BH[0][i].to_csv(r'car_data_BH_Q_44')
    car_data_BH[1][i].to_csv(r'car_data_BH_Q_63')
    car_data_BH[2][i].to_csv(r'car_data_BH_Q_1')
    car_data_BH[3][i].to_csv(r'car_data_BH_Q_11')
    car_data_BH[4][i].to_csv(r'car_data_BH_Q_16')
    car_data_BH[5][i].to_csv(r'car_data_BH_Q_55')
    car_data_BH[6][i].to_csv(r'car_data_BH_Q_4')
    car_data_BH[7][i].to_csv(r'car_data_BH_Q_3')
    car_data_BH[8][i].to_csv(r'car_data_BH_Q_14')
    car_data_BH[9][i].to_csv(r'car_data_BH_Q_31')
    car_data_BH[10][i].to_csv(r'car_data_BH_Q_10')
    car_data_BH[11][i].to_csv(r'car_data_BH_Q_22')
    car_data_BH[12][i].to_csv(r'car_data_BH_Q_5')
    car_data_BH[13][i].to_csv(r'car_data_BH_Q_18')
    car_data_BH[14][i].to_csv(r'car_data_BH_Q_77')
    car_data_BH[15][i].to_csv(r'car_data_BH_Q_24')
    car_data_BH[16][i].to_csv(r'car_data_BH_Q_23')
    car_data_BH[17][i].to_csv(r'car_data_BH_Q_6')
    car_data_BH[18][i].to_csv(r'car_data_BH_Q_20')
    car_data_BH[19][i].to_csv(r'car_data_BH_Q_47')

    i = 4
    car_data_BH[0][i].to_csv(r'car_data_BH_R_44')
    car_data_BH[1][i].to_csv(r'car_data_BH_R_63')
    car_data_BH[2][i].to_csv(r'car_data_BH_R_1')
    car_data_BH[3][i].to_csv(r'car_data_BH_R_11')
    car_data_BH[4][i].to_csv(r'car_data_BH_R_16')
    car_data_BH[5][i].to_csv(r'car_data_BH_R_55')
    car_data_BH[6][i].to_csv(r'car_data_BH_R_4')
    car_data_BH[7][i].to_csv(r'car_data_BH_R_3')
    car_data_BH[8][i].to_csv(r'car_data_BH_R_14')
    car_data_BH[9][i].to_csv(r'car_data_BH_R_31')
    car_data_BH[10][i].to_csv(r'car_data_BH_R_10')
    car_data_BH[11][i].to_csv(r'car_data_BH_R_22')
    car_data_BH[12][i].to_csv(r'car_data_BH_R_5')
    car_data_BH[13][i].to_csv(r'car_data_BH_R_18')
    car_data_BH[14][i].to_csv(r'car_data_BH_R_77')
    car_data_BH[15][i].to_csv(r'car_data_BH_R_24')
    car_data_BH[16][i].to_csv(r'car_data_BH_R_23')
    car_data_BH[17][i].to_csv(r'car_data_BH_R_6')
    car_data_BH[18][i].to_csv(r'car_data_BH_R_20')
    car_data_BH[19][i].to_csv(r'car_data_BH_R_47')
    return
#-----------------------------------------------------------------------------------------------------------------------
def Car_data_SA():
    i = 0
    car_data_SA[0][i] = car_data_SA_FP1["44"]
    car_data_SA[1][i] = car_data_SA_FP1["63"]
    car_data_SA[2][i] = car_data_SA_FP1["1"]
    car_data_SA[3][i] = car_data_SA_FP1["11"]
    car_data_SA[4][i] = car_data_SA_FP1["16"]
    car_data_SA[5][i] = car_data_SA_FP1["55"]
    car_data_SA[6][i] = car_data_SA_FP1["3"]
    car_data_SA[7][i] = car_data_SA_FP1["4"]
    car_data_SA[8][i] = car_data_SA_FP1["14"]
    car_data_SA[9][i] = car_data_SA_FP1["31"]
    car_data_SA[10][i] = car_data_SA_FP1["10"]
    car_data_SA[11][i] = car_data_SA_FP1["22"]
    # car_data_BH[11][i] = car_data_SA_FP1["5"]
    car_data_SA[12][i] = car_data_SA_FP1["27"]
    car_data_SA[13][i] = car_data_SA_FP1["18"]
    car_data_SA[14][i] = car_data_SA_FP1["77"]
    car_data_SA[15][i] = car_data_SA_FP1["24"]
    car_data_SA[16][i] = car_data_SA_FP1["23"]
    car_data_SA[17][i] = car_data_SA_FP1["6"]
    car_data_SA[18][i] = car_data_SA_FP1["20"]
    car_data_SA[19][i] = car_data_SA_FP1["47"]

    i = 1
    car_data_SA[0][i] = car_data_SA_FP2["44"]
    car_data_SA[1][i] = car_data_SA_FP2["63"]
    car_data_SA[2][i] = car_data_SA_FP2["1"]
    car_data_SA[3][i] = car_data_SA_FP2["11"]
    car_data_SA[4][i] = car_data_SA_FP2["16"]
    car_data_SA[5][i] = car_data_SA_FP2["55"]
    car_data_SA[6][i] = car_data_SA_FP2["3"]
    car_data_SA[7][i] = car_data_SA_FP2["4"]
    car_data_SA[8][i] = car_data_SA_FP2["14"]
    car_data_SA[9][i] = car_data_SA_FP2["31"]
    car_data_SA[10][i] = car_data_SA_FP2["10"]
    car_data_SA[11][i] = car_data_SA_FP2["22"]
    # car_data_SA[11][i] = car_data_SA_FP2["5"]
    car_data_SA[12][i] = car_data_SA_FP2["27"]
    car_data_SA[13][i] = car_data_SA_FP2["18"]
    car_data_SA[14][i] = car_data_SA_FP2["77"]
    car_data_SA[15][i] = car_data_SA_FP2["24"]
    car_data_SA[16][i] = car_data_SA_FP2["23"]
    car_data_SA[17][i] = car_data_SA_FP2["6"]
    car_data_SA[18][i] = car_data_SA_FP2["20"]
    car_data_SA[19][i] = car_data_SA_FP2["47"]

    i = 2
    car_data_SA[0][i] = car_data_SA_FP3["44"]
    car_data_SA[1][i] = car_data_SA_FP3["63"]
    car_data_SA[2][i] = car_data_SA_FP3["1"]
    car_data_SA[3][i] = car_data_SA_FP3["11"]
    car_data_SA[4][i] = car_data_SA_FP3["16"]
    car_data_SA[5][i] = car_data_SA_FP3["55"]
    car_data_SA[6][i] = car_data_SA_FP3["3"]
    car_data_SA[7][i] = car_data_SA_FP3["4"]
    car_data_SA[8][i] = car_data_SA_FP3["14"]
    car_data_SA[9][i] = car_data_SA_FP3["31"]
    car_data_SA[10][i] = car_data_SA_FP3["10"]
    car_data_SA[11][i] = car_data_SA_FP3["22"]
    # car_data_SA[11][i] = car_data_BH_FP3["5"]
    car_data_SA[12][i] = car_data_SA_FP3["27"]
    car_data_SA[13][i] = car_data_SA_FP3["18"]
    car_data_SA[14][i] = car_data_SA_FP3["77"]
    car_data_SA[15][i] = car_data_SA_FP3["24"]
    car_data_SA[16][i] = car_data_SA_FP3["23"]
    car_data_SA[17][i] = car_data_SA_FP3["6"]
    car_data_SA[18][i] = car_data_SA_FP3["20"]
    car_data_SA[19][i] = car_data_SA_FP3["47"]

    i = 3
    car_data_SA[0][i] = car_data_SA_Q["44"]
    car_data_SA[1][i] = car_data_SA_Q["63"]
    car_data_SA[2][i] = car_data_SA_Q["1"]
    car_data_SA[3][i] = car_data_SA_Q["11"]
    car_data_SA[4][i] = car_data_SA_Q["16"]
    car_data_SA[5][i] = car_data_SA_Q["55"]
    car_data_SA[6][i] = car_data_SA_Q["3"]
    car_data_SA[7][i] = car_data_SA_Q["4"]
    car_data_SA[8][i] = car_data_SA_Q["14"]
    car_data_SA[9][i] = car_data_SA_Q["31"]
    car_data_SA[10][i] = car_data_SA_Q["10"]
    car_data_SA[11][i] = car_data_SA_Q["22"]
    # car_data_SA[11][i] = car_data_SA_Q["5"]
    car_data_SA[12][i] = car_data_SA_Q["27"]
    car_data_SA[13][i] = car_data_SA_Q["18"]
    car_data_SA[14][i] = car_data_SA_Q["77"]
    car_data_SA[15][i] = car_data_SA_Q["24"]
    car_data_SA[16][i] = car_data_SA_Q["23"]
    car_data_SA[17][i] = car_data_SA_Q["6"]
    car_data_SA[18][i] = car_data_SA_Q["20"]
    car_data_SA[19][i] = car_data_SA_Q["47"]

    i = 4
    car_data_SA[0][i] = car_data_SA_R["44"]
    car_data_SA[1][i] = car_data_SA_R["63"]
    car_data_SA[2][i] = car_data_SA_R["1"]
    car_data_SA[3][i] = car_data_SA_R["11"]
    car_data_SA[4][i] = car_data_SA_R["16"]
    car_data_SA[5][i] = car_data_SA_R["55"]
    car_data_SA[6][i] = car_data_SA_R["3"]
    car_data_SA[7][i] = car_data_SA_R["4"]
    car_data_SA[8][i] = car_data_SA_R["14"]
    car_data_SA[9][i] = car_data_SA_R["31"]
    car_data_SA[10][i] = car_data_SA_R["10"]
    car_data_SA[11][i] = car_data_SA_R["22"]
    # car_data_SA[11][i] = car_data_SA_R["5"]
    car_data_SA[12][i] = car_data_SA_R["27"]
    car_data_SA[13][i] = car_data_SA_R["18"]
    car_data_SA[14][i] = car_data_SA_R["77"]
    car_data_SA[15][i] = car_data_SA_R["24"]
    car_data_SA[16][i] = car_data_SA_R["23"]
    car_data_SA[17][i] = car_data_SA_R["6"]
    car_data_SA[18][i] = car_data_SA_R["20"]
    car_data_SA[19][i] = car_data_SA_R["47"]
    return

def Car_data_SA_Writer():
    i = 0
    car_data_SA[0][i].to_csv(r'car_data_SA_FP1_44')
    car_data_SA[1][i].to_csv(r'car_data_SA_FP1_63')
    car_data_SA[2][i].to_csv(r'car_data_SA_FP1_1')
    car_data_SA[3][i].to_csv(r'car_data_SA_FP1_11')
    car_data_SA[4][i].to_csv(r'car_data_SA_FP1_16')
    car_data_SA[5][i].to_csv(r'car_data_SA_FP1_55')
    car_data_SA[6][i].to_csv(r'car_data_SA_FP1_4')
    car_data_SA[7][i].to_csv(r'car_data_SA_FP1_3')
    car_data_SA[8][i].to_csv(r'car_data_SA_FP1_14')
    car_data_SA[9][i].to_csv(r'car_data_SA_FP1_31')
    car_data_SA[10][i].to_csv(r'car_data_SA_FP1_10')
    car_data_SA[11][i].to_csv(r'car_data_SA_FP1_22')
    car_data_SA[12][i].to_csv(r'car_data_SA_FP1_5')
    car_data_SA[13][i].to_csv(r'car_data_SA_FP1_18')
    car_data_SA[14][i].to_csv(r'car_data_SA_FP1_77')
    car_data_SA[15][i].to_csv(r'car_data_SA_FP1_24')
    car_data_SA[16][i].to_csv(r'car_data_SA_FP1_23')
    car_data_SA[17][i].to_csv(r'car_data_SA_FP1_6')
    car_data_SA[18][i].to_csv(r'car_data_SA_FP1_20')
    car_data_SA[19][i].to_csv(r'car_data_SA_FP1_47')

    i = 1
    car_data_SA[0][i].to_csv(r'car_data_SA_FP2_44')
    car_data_SA[1][i].to_csv(r'car_data_SA_FP2_63')
    car_data_SA[2][i].to_csv(r'car_data_SA_FP2_1')
    car_data_SA[3][i].to_csv(r'car_data_SA_FP2_11')
    car_data_SA[4][i].to_csv(r'car_data_SA_FP2_16')
    car_data_SA[5][i].to_csv(r'car_data_SA_FP2_55')
    car_data_SA[6][i].to_csv(r'car_data_SA_FP2_4')
    car_data_SA[7][i].to_csv(r'car_data_SA_FP2_3')
    car_data_SA[8][i].to_csv(r'car_data_SA_FP2_14')
    car_data_SA[9][i].to_csv(r'car_data_SA_FP2_31')
    car_data_SA[10][i].to_csv(r'car_data_SA_FP2_10')
    car_data_SA[11][i].to_csv(r'car_data_SA_FP2_22')
    car_data_SA[12][i].to_csv(r'car_data_SA_FP2_5')
    car_data_SA[13][i].to_csv(r'car_data_SA_FP2_18')
    car_data_SA[14][i].to_csv(r'car_data_SA_FP2_77')
    car_data_SA[15][i].to_csv(r'car_data_SA_FP2_24')
    car_data_SA[16][i].to_csv(r'car_data_SA_FP2_23')
    car_data_SA[17][i].to_csv(r'car_data_SA_FP2_6')
    car_data_SA[18][i].to_csv(r'car_data_SA_FP2_20')
    car_data_SA[19][i].to_csv(r'car_data_SA_FP2_47')

    i = 2
    car_data_SA[0][i].to_csv(r'car_data_SA_FP3_44')
    car_data_SA[1][i].to_csv(r'car_data_SA_FP3_63')
    car_data_SA[2][i].to_csv(r'car_data_SA_FP3_1')
    car_data_SA[3][i].to_csv(r'car_data_SA_FP3_11')
    car_data_SA[4][i].to_csv(r'car_data_SA_FP3_16')
    car_data_SA[5][i].to_csv(r'car_data_SA_FP3_55')
    car_data_SA[6][i].to_csv(r'car_data_SA_FP3_4')
    car_data_SA[7][i].to_csv(r'car_data_SA_FP3_3')
    car_data_SA[8][i].to_csv(r'car_data_SA_FP3_14')
    car_data_SA[9][i].to_csv(r'car_data_SA_FP3_31')
    car_data_SA[10][i].to_csv(r'car_data_SA_FP3_10')
    car_data_SA[11][i].to_csv(r'car_data_SA_FP3_22')
    car_data_SA[12][i].to_csv(r'car_data_SA_FP3_5')
    car_data_SA[13][i].to_csv(r'car_data_SA_FP3_18')
    car_data_SA[14][i].to_csv(r'car_data_SA_FP3_77')
    car_data_SA[15][i].to_csv(r'car_data_SA_FP3_24')
    car_data_SA[16][i].to_csv(r'car_data_SA_FP3_23')
    car_data_SA[17][i].to_csv(r'car_data_SA_FP3_6')
    car_data_SA[18][i].to_csv(r'car_data_SA_FP3_20')
    car_data_SA[19][i].to_csv(r'car_data_SA_FP3_47')

    i = 3
    car_data_SA[0][i].to_csv(r'car_data_SA_Q_44')
    car_data_SA[1][i].to_csv(r'car_data_SA_Q_63')
    car_data_SA[2][i].to_csv(r'car_data_SA_Q_1')
    car_data_SA[3][i].to_csv(r'car_data_SA_Q_11')
    car_data_SA[4][i].to_csv(r'car_data_SA_Q_16')
    car_data_SA[5][i].to_csv(r'car_data_SA_Q_55')
    car_data_SA[6][i].to_csv(r'car_data_SA_Q_4')
    car_data_SA[7][i].to_csv(r'car_data_SA_Q_3')
    car_data_SA[8][i].to_csv(r'car_data_SA_Q_14')
    car_data_SA[9][i].to_csv(r'car_data_SA_Q_31')
    car_data_SA[10][i].to_csv(r'car_data_SA_Q_10')
    car_data_SA[11][i].to_csv(r'car_data_SA_Q_22')
    car_data_SA[12][i].to_csv(r'car_data_SA_Q_5')
    car_data_SA[13][i].to_csv(r'car_data_SA_Q_18')
    car_data_SA[14][i].to_csv(r'car_data_SA_Q_77')
    car_data_SA[15][i].to_csv(r'car_data_SA_Q_24')
    car_data_SA[16][i].to_csv(r'car_data_SA_Q_23')
    car_data_SA[17][i].to_csv(r'car_data_SA_Q_6')
    car_data_SA[18][i].to_csv(r'car_data_SA_Q_20')
    car_data_SA[19][i].to_csv(r'car_data_SA_Q_47')

    i = 4
    car_data_SA[0][i].to_csv(r'car_data_SA_R_44')
    car_data_SA[1][i].to_csv(r'car_data_SA_R_63')
    car_data_SA[2][i].to_csv(r'car_data_SA_R_1')
    car_data_SA[3][i].to_csv(r'car_data_SA_R_11')
    car_data_SA[4][i].to_csv(r'car_data_SA_R_16')
    car_data_SA[5][i].to_csv(r'car_data_SA_R_55')
    car_data_SA[6][i].to_csv(r'car_data_SA_R_4')
    car_data_SA[7][i].to_csv(r'car_data_SA_R_3')
    car_data_SA[8][i].to_csv(r'car_data_SA_R_14')
    car_data_SA[9][i].to_csv(r'car_data_SA_R_31')
    car_data_SA[10][i].to_csv(r'car_data_SA_R_10')
    car_data_SA[11][i].to_csv(r'car_data_SA_R_22')
    car_data_SA[12][i].to_csv(r'car_data_SA_R_5')
    car_data_SA[13][i].to_csv(r'car_data_SA_R_18')
    car_data_SA[14][i].to_csv(r'car_data_SA_R_77')
    car_data_SA[15][i].to_csv(r'car_data_SA_R_24')
    car_data_SA[16][i].to_csv(r'car_data_SA_R_23')
    car_data_SA[17][i].to_csv(r'car_data_SA_R_6')
    car_data_SA[18][i].to_csv(r'car_data_SA_R_20')
    car_data_SA[19][i].to_csv(r'car_data_SA_R_47')
    return
#-----------------------------------------------------------------------------------------------------------------------
def Car_data_AU():
    i = 0
    car_data_AU[0][i] = car_data_AU_FP1["44"]
    car_data_AU[1][i] = car_data_AU_FP1["63"]
    car_data_AU[2][i] = car_data_AU_FP1["1"]
    car_data_AU[3][i] = car_data_AU_FP1["11"]
    car_data_AU[4][i] = car_data_AU_FP1["16"]
    car_data_AU[5][i] = car_data_AU_FP1["55"]
    car_data_AU[6][i] = car_data_AU_FP1["3"]
    car_data_AU[7][i] = car_data_AU_FP1["4"]
    car_data_AU[8][i] = car_data_AU_FP1["14"]
    car_data_AU[9][i] = car_data_AU_FP1["31"]
    car_data_AU[10][i] = car_data_AU_FP1["10"]
    car_data_AU[11][i] = car_data_AU_FP1["22"]
    car_data_AU[12][i] = car_data_AU_FP1["5"]
    #car_data_AU[12][i] = car_data_AU_FP1["27"]
    car_data_AU[13][i] = car_data_AU_FP1["18"]
    car_data_AU[14][i] = car_data_AU_FP1["77"]
    car_data_AU[15][i] = car_data_AU_FP1["24"]
    car_data_AU[16][i] = car_data_AU_FP1["23"]
    car_data_AU[17][i] = car_data_AU_FP1["6"]
    car_data_AU[18][i] = car_data_AU_FP1["9"]
    car_data_AU[19][i] = car_data_AU_FP1["47"]

    i = 1
    car_data_AU[0][i] = car_data_AU_FP2["44"]
    car_data_AU[1][i] = car_data_AU_FP2["63"]
    car_data_AU[2][i] = car_data_AU_FP2["1"]
    car_data_AU[3][i] = car_data_AU_FP2["11"]
    car_data_AU[4][i] = car_data_AU_FP2["16"]
    car_data_AU[5][i] = car_data_AU_FP2["55"]
    car_data_AU[6][i] = car_data_AU_FP2["3"]
    car_data_AU[7][i] = car_data_AU_FP2["4"]
    car_data_AU[8][i] = car_data_AU_FP2["14"]
    car_data_AU[9][i] = car_data_AU_FP2["31"]
    car_data_AU[10][i] = car_data_AU_FP2["10"]
    car_data_AU[11][i] = car_data_AU_FP2["22"]
    car_data_AU[12][i] = car_data_AU_FP2["5"]
    #car_data_AU[12][i] = car_data_AU_FP2["27"]
    car_data_AU[13][i] = car_data_AU_FP2["18"]
    car_data_AU[14][i] = car_data_AU_FP2["77"]
    car_data_AU[15][i] = car_data_AU_FP2["24"]
    car_data_AU[16][i] = car_data_AU_FP2["23"]
    car_data_AU[17][i] = car_data_AU_FP2["6"]
    car_data_AU[18][i] = car_data_AU_FP2["9"]
    car_data_AU[19][i] = car_data_AU_FP2["47"]

    i = 2
    car_data_AU[0][i] = car_data_AU_FP3["44"]
    car_data_AU[1][i] = car_data_AU_FP3["63"]
    car_data_AU[2][i] = car_data_AU_FP3["1"]
    car_data_AU[3][i] = car_data_AU_FP3["11"]
    car_data_AU[4][i] = car_data_AU_FP3["16"]
    car_data_AU[5][i] = car_data_AU_FP3["55"]
    car_data_AU[6][i] = car_data_AU_FP3["3"]
    car_data_AU[7][i] = car_data_AU_FP3["4"]
    car_data_AU[8][i] = car_data_AU_FP3["14"]
    car_data_AU[9][i] = car_data_AU_FP3["31"]
    car_data_AU[10][i] = car_data_AU_FP3["10"]
    car_data_AU[11][i] = car_data_AU_FP3["22"]
    car_data_AU[12][i] = car_data_AU_FP3["5"]
    #car_data_AU[12][i] = car_data_AU_FP3["27"]
    car_data_AU[13][i] = car_data_AU_FP3["18"]
    car_data_AU[14][i] = car_data_AU_FP3["77"]
    car_data_AU[15][i] = car_data_AU_FP3["24"]
    car_data_AU[16][i] = car_data_AU_FP3["23"]
    car_data_AU[17][i] = car_data_AU_FP3["6"]
    car_data_AU[18][i] = car_data_AU_FP3["20"]
    car_data_AU[19][i] = car_data_AU_FP3["47"]

    i = 3
    car_data_AU[0][i] = car_data_AU_Q["44"]
    car_data_AU[1][i] = car_data_AU_Q["63"]
    car_data_AU[2][i] = car_data_AU_Q["1"]
    car_data_AU[3][i] = car_data_AU_Q["11"]
    car_data_AU[4][i] = car_data_AU_Q["16"]
    car_data_AU[5][i] = car_data_AU_Q["55"]
    car_data_AU[6][i] = car_data_AU_Q["3"]
    car_data_AU[7][i] = car_data_AU_Q["4"]
    car_data_AU[8][i] = car_data_AU_Q["14"]
    car_data_AU[9][i] = car_data_AU_Q["31"]
    car_data_AU[10][i] = car_data_AU_Q["10"]
    car_data_AU[11][i] = car_data_AU_Q["22"]
    car_data_AU[12][i] = car_data_AU_Q["5"]
    #car_data_AU[12][i] = car_data_AU_Q["27"]
    car_data_AU[13][i] = car_data_AU_Q["18"]
    car_data_AU[14][i] = car_data_AU_Q["77"]
    car_data_AU[15][i] = car_data_AU_Q["24"]
    car_data_AU[16][i] = car_data_AU_Q["23"]
    car_data_AU[17][i] = car_data_AU_Q["6"]
    car_data_AU[18][i] = car_data_AU_Q["20"]
    car_data_AU[19][i] = car_data_AU_Q["47"]

    i = 4
    car_data_AU[0][i] = car_data_AU_R["44"]
    car_data_AU[1][i] = car_data_AU_R["63"]
    car_data_AU[2][i] = car_data_AU_R["1"]
    car_data_AU[3][i] = car_data_AU_R["11"]
    car_data_AU[4][i] = car_data_AU_R["16"]
    car_data_AU[5][i] = car_data_AU_R["55"]
    car_data_AU[6][i] = car_data_AU_R["3"]
    car_data_AU[7][i] = car_data_AU_R["4"]
    car_data_AU[8][i] = car_data_AU_R["14"]
    car_data_AU[9][i] = car_data_AU_R["31"]
    car_data_AU[10][i] = car_data_AU_R["10"]
    car_data_AU[11][i] = car_data_AU_R["22"]
    car_data_AU[12][i] = car_data_AU_R["5"]
    #car_data_AU[12][i] = car_data_AU_R["27"]
    car_data_AU[13][i] = car_data_AU_R["18"]
    car_data_AU[14][i] = car_data_AU_R["77"]
    car_data_AU[15][i] = car_data_AU_R["24"]
    car_data_AU[16][i] = car_data_AU_R["23"]
    car_data_AU[17][i] = car_data_AU_R["6"]
    car_data_AU[18][i] = car_data_AU_R["20"]
    car_data_AU[19][i] = car_data_AU_R["47"]
    return

def Car_data_AU_Writer():
    i = 0
    car_data_AU[0][i].to_csv(r'car_data_AU_FP1_44')
    car_data_AU[1][i].to_csv(r'car_data_AU_FP1_63')
    car_data_AU[2][i].to_csv(r'car_data_AU_FP1_1')
    car_data_AU[3][i].to_csv(r'car_data_AU_FP1_11')
    car_data_AU[4][i].to_csv(r'car_data_AU_FP1_16')
    car_data_AU[5][i].to_csv(r'car_data_AU_FP1_55')
    car_data_AU[6][i].to_csv(r'car_data_AU_FP1_4')
    car_data_AU[7][i].to_csv(r'car_data_AU_FP1_3')
    car_data_AU[8][i].to_csv(r'car_data_AU_FP1_14')
    car_data_AU[9][i].to_csv(r'car_data_AU_FP1_31')
    car_data_AU[10][i].to_csv(r'car_data_AU_FP1_10')
    car_data_AU[11][i].to_csv(r'car_data_AU_FP1_22')
    pd.DataFrame({'condition' : ["No data found"]}).to_csv(r'car_data_AU_FP1_5')
    car_data_AU[13][i].to_csv(r'car_data_AU_FP1_18')
    car_data_AU[14][i].to_csv(r'car_data_AU_FP1_77')
    car_data_AU[15][i].to_csv(r'car_data_AU_FP1_24')
    car_data_AU[16][i].to_csv(r'car_data_AU_FP1_23')
    car_data_AU[17][i].to_csv(r'car_data_AU_FP1_6')
    car_data_AU[18][i].to_csv(r'car_data_AU_FP1_20')
    car_data_AU[19][i].to_csv(r'car_data_AU_FP1_47')

    i = 1
    car_data_AU[0][i].to_csv(r'car_data_AU_FP2_44')
    car_data_AU[1][i].to_csv(r'car_data_AU_FP2_63')
    car_data_AU[2][i].to_csv(r'car_data_AU_FP2_1')
    car_data_AU[3][i].to_csv(r'car_data_AU_FP2_11')
    car_data_AU[4][i].to_csv(r'car_data_AU_FP2_16')
    car_data_AU[5][i].to_csv(r'car_data_AU_FP2_55')
    car_data_AU[6][i].to_csv(r'car_data_AU_FP2_4')
    car_data_AU[7][i].to_csv(r'car_data_AU_FP2_3')
    car_data_AU[8][i].to_csv(r'car_data_AU_FP2_14')
    car_data_AU[9][i].to_csv(r'car_data_AU_FP2_31')
    car_data_AU[10][i].to_csv(r'car_data_AU_FP2_10')
    car_data_AU[11][i].to_csv(r'car_data_AU_FP2_22')
    pd.DataFrame({'condition' : ["No data found"]}).to_csv(r'car_data_AU_FP2_5')
    car_data_AU[13][i].to_csv(r'car_data_AU_FP2_18')
    car_data_AU[14][i].to_csv(r'car_data_AU_FP2_77')
    car_data_AU[15][i].to_csv(r'car_data_AU_FP2_24')
    car_data_AU[16][i].to_csv(r'car_data_AU_FP2_23')
    car_data_AU[17][i].to_csv(r'car_data_AU_FP2_6')
    car_data_AU[18][i].to_csv(r'car_data_AU_FP2_20')
    car_data_AU[19][i].to_csv(r'car_data_AU_FP2_47')

    i = 2
    car_data_AU[0][i].to_csv(r'car_data_AU_FP3_44')
    car_data_AU[1][i].to_csv(r'car_data_AU_FP3_63')
    car_data_AU[2][i].to_csv(r'car_data_AU_FP3_1')
    car_data_AU[3][i].to_csv(r'car_data_AU_FP3_11')
    car_data_AU[4][i].to_csv(r'car_data_AU_FP3_16')
    car_data_AU[5][i].to_csv(r'car_data_AU_FP3_55')
    car_data_AU[6][i].to_csv(r'car_data_AU_FP3_4')
    car_data_AU[7][i].to_csv(r'car_data_AU_FP3_3')
    car_data_AU[8][i].to_csv(r'car_data_AU_FP3_14')
    car_data_AU[9][i].to_csv(r'car_data_AU_FP3_31')
    car_data_AU[10][i].to_csv(r'car_data_AU_FP3_10')
    car_data_AU[11][i].to_csv(r'car_data_AU_FP3_22')
    pd.DataFrame({'condition' : ["No data found"]}).to_csv(r'car_data_AU_FP3_5')
    car_data_AU[13][i].to_csv(r'car_data_AU_FP3_18')
    car_data_AU[14][i].to_csv(r'car_data_AU_FP3_77')
    car_data_AU[15][i].to_csv(r'car_data_AU_FP3_24')
    car_data_AU[16][i].to_csv(r'car_data_AU_FP3_23')
    car_data_AU[17][i].to_csv(r'car_data_AU_FP3_6')
    car_data_AU[18][i].to_csv(r'car_data_AU_FP3_20')
    car_data_AU[19][i].to_csv(r'car_data_AU_FP3_47')

    i = 3
    car_data_AU[0][i].to_csv(r'car_data_AU_Q_44')
    car_data_AU[1][i].to_csv(r'car_data_AU_Q_63')
    car_data_AU[2][i].to_csv(r'car_data_AU_Q_1')
    car_data_AU[3][i].to_csv(r'car_data_AU_Q_11')
    car_data_AU[4][i].to_csv(r'car_data_AU_Q_16')
    car_data_AU[5][i].to_csv(r'car_data_AU_Q_55')
    car_data_AU[6][i].to_csv(r'car_data_AU_Q_4')
    car_data_AU[7][i].to_csv(r'car_data_AU_Q_3')
    car_data_AU[8][i].to_csv(r'car_data_AU_Q_14')
    car_data_AU[9][i].to_csv(r'car_data_AU_Q_31')
    car_data_AU[10][i].to_csv(r'car_data_AU_Q_10')
    car_data_AU[11][i].to_csv(r'car_data_AU_Q_22')
    pd.DataFrame({'condition' : ["No data found"]}).to_csv(r'car_data_AU_Q_5')
    car_data_AU[13][i].to_csv(r'car_data_AU_Q_18')
    car_data_AU[14][i].to_csv(r'car_data_AU_Q_77')
    car_data_AU[15][i].to_csv(r'car_data_AU_Q_24')
    car_data_AU[16][i].to_csv(r'car_data_AU_Q_23')
    car_data_AU[17][i].to_csv(r'car_data_AU_Q_6')
    car_data_AU[18][i].to_csv(r'car_data_AU_Q_20')
    car_data_AU[19][i].to_csv(r'car_data_AU_Q_47')

    i = 4
    car_data_AU[0][i].to_csv(r'car_data_AU_R_44')
    car_data_AU[1][i].to_csv(r'car_data_AU_R_63')
    car_data_AU[2][i].to_csv(r'car_data_AU_R_1')
    car_data_AU[3][i].to_csv(r'car_data_AU_R_11')
    car_data_AU[4][i].to_csv(r'car_data_AU_R_16')
    car_data_AU[5][i].to_csv(r'car_data_AU_R_55')
    car_data_AU[6][i].to_csv(r'car_data_AU_R_4')
    car_data_AU[7][i].to_csv(r'car_data_AU_R_3')
    car_data_AU[8][i].to_csv(r'car_data_AU_R_14')
    car_data_AU[9][i].to_csv(r'car_data_AU_R_31')
    car_data_AU[10][i].to_csv(r'car_data_AU_R_10')
    car_data_AU[11][i].to_csv(r'car_data_AU_R_22')
    pd.DataFrame({'condition' : ["No data found"]}).to_csv(r'car_data_AU_R_5')
    car_data_AU[13][i].to_csv(r'car_data_AU_R_18')
    car_data_AU[14][i].to_csv(r'car_data_AU_R_77')
    car_data_AU[15][i].to_csv(r'car_data_AU_R_24')
    car_data_AU[16][i].to_csv(r'car_data_AU_R_23')
    car_data_AU[17][i].to_csv(r'car_data_AU_R_6')
    car_data_AU[18][i].to_csv(r'car_data_AU_R_20')
    car_data_AU[19][i].to_csv(r'car_data_AU_R_47')
    return
#-----------------------------------------------------------------------------------------------------------------------
def main():
    #the function names are timing_data_BH_O as "oh"
    #and timing_data_BH_I as the upper case of "i"
    #this is because otherwise the function name is
    #the same as the list name
    #and causes the error below:
    #TypeError: 'function' object is not subscriptable
    #print(car_data_BH_FP1['1']) = the car data set for max verstappen in python dataframe
    #print(type(car_data_BH_FP1['1'])) = python data frame
    #Car_data_BH()
    #Car_data_BH_Writer()

    #Car_data_SA()
    #Car_data_SA_Writer()

    #Car_data_AU()
    #Car_data_AU_Writer()
    print("done")
    return
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()