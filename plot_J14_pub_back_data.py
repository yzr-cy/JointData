import matplotlib.pyplot as plt
import pandas as pd
import os



path = os.path.dirname(__file__)


data = pd.read_csv(path + '/hit_robotJ14_pub_data.csv')
# data_back = pd.read_csv(path + '/J14_back_data.csv')
# data_com = pd.read_csv(path + '/com_data.csv')


indexL = [0, 1, 2, 3, 4, 5] #左腿索引
indexR = [6, 7, 8, 9, 10, 11] #左腿索引
indexWaist = [12, 13]

# indexL_back = [3, 4, 7, 8, 9, 10] #左腿索引
# indexR_back = [5, 6, 11, 12, 13, 14] #左腿索引


Jname = [ 
         'JleftHip_roll', 'JleftHip_yaw', 'JleftHip_pitch', 'JleftKnee_pitch','JleftAnkle_pitch','JleftAnkle_roll',
         'JrightHip_roll', 'JrightHip_yaw', 'JrightHip_pitch', 'JrightKnee_pitch', 'JrightAnkle_pitch', 'JrightAnkle_roll',
         'Jwaist_yaw', 'Jwaist_pitch',
         ]
i = 0
fig, (ax1, ax2, ax3) = plt.subplots(3)

plotRec = False

print(len(Jname))
print(data.shape[1])
if(len(Jname) == data.shape[1]-1):
    # time = data.iloc[:,0]
    # time_back = data_back.iloc[:,0]
    # 画全部
    # while i < data.shape[1]:
    #     col = data.iloc[:,i]
    #     plt.plot(col,label = Jname[i])
    #     i = i+1
    # 画选择到的
    for i in indexL:
        col = data.iloc[:,i]
        ax1.plot(col.values,label = Jname[i])
    

    for i in indexR:
        col = data.iloc[:,i]
        ax2.plot(col.values,label = Jname[i])
    
    for i in indexWaist:
        col = data.iloc[:,i]
        ax3.plot(col.values,label = Jname[i])
    # ax3.plot(data_com.iloc[:,0].values,data_com.iloc[:,1].values)
    ax1.legend()
    ax2.legend()
    ax3.legend()
    plt.tight_layout()
    plt.show()
else:
    print("数据列数和名称个数不匹配")