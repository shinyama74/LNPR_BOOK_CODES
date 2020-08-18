import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_csv(r"C:\Users\u904989i\PycharmProjects\LNPR_BOOK_CODES\section_sensor\sensor_data_200.txt", delimiter=" ", header=None, names= ("date","time","ir","lidar"))

data["lidar"].hist(bins= max(data["lidar"])-min(data["lidar"]), align='left',color='orange')

mean1=sum(data['lidar'].values)/len(data['lidar'].values)
mean2= data['lidar'].mean()

plt.vlines(mean1 , ymin=0, ymax=5000 , color='red')
plt.show()

# print(data["lidar"][0:7])

#分散について
zs=data['lidar'].values
mean=sum(zs)/len(zs)
diff_square=[(z-mean)**2 for z in zs]

sampling_var=sum(diff_square)/len(zs)        #標本分散
unbiased_var= sum(diff_square)/(len(zs)-1)   #不偏分散

#by Pandas
pandas_sampling_var = data['lidar'].var(ddof=False)        #標本分散
pandas_unbiased_var = data['lidar'].var()   #不偏分散

#by Numpy
numpy_sampling_var = np.var(data['lidar'])       #標本分散
numpy_unbiased_var = np.var(data['lidar'],ddof = 1)   #不偏分散

print(sampling_var)
print(unbiased_var)
print(pandas_sampling_var)
print(pandas_unbiased_var)
print(numpy_sampling_var)
print(numpy_unbiased_var)
