import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np


df = pd.read_csv('data/C2A2_data/BinnedCsvs_d25/391a2922ad597ba080f4b99dea6d62842562d64845ef5df1a384561e.csv')
df['Y'], df['M-D'] = zip(*df['Date'].apply(lambda x: (x[:4], x[5:])))
df = df[df['M-D'] != '02-29']
temp_min = df[(df['Element'] == 'TMIN') & (df['Y'] != '2015')].groupby('M-D').aggregate({'Data_Value':np.min})
temp_max = df[(df['Element'] == 'TMAX') & (df['Y'] != '2015')].groupby('M-D').aggregate({'Data_Value':np.max})
temp_min_15 = df[(df['Element'] == 'TMIN') & (df['Y'] == '2015')].groupby('M-D').aggregate({'Data_Value':np.min})
temp_max_15 = df[(df['Element'] == 'TMAX') & (df['Y'] == '2015')].groupby('M-D').aggregate({'Data_Value':np.max})
broken_min = np.where(temp_min_15['Data_Value'] < temp_min['Data_Value'])[0]
broken_max = np.where(temp_max_15['Data_Value'] > temp_max['Data_Value'])[0]

plt.figure()
plt.plot(temp_min.values, 'lightblue', label = 'Record Low')
plt.plot(temp_max.values, 'lightgreen', label = 'Record High')
plt.scatter(broken_min, temp_min_15.iloc[broken_min], s = 10, c = 'brown', label = 'Broken Low')
plt.scatter(broken_max, temp_max_15.iloc[broken_max], s = 10, c = 'magenta', label = 'Broken High')
plt.gca().axis([-5, 400, -750, 750])
plt.xticks(range(0, len(temp_min), 20), temp_min.index[range(0, len(temp_min), 20)], rotation = '45')
plt.xlabel('Day of the Year')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.title('Temperature Summary Plot near Kanpur')
plt.legend(loc = 4, frameon = False)
plt.gca().fill_between(range(len(temp_min)), temp_min['Data_Value'], temp_max['Data_Value'], facecolor = 'yellow', alpha = 0.2)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
