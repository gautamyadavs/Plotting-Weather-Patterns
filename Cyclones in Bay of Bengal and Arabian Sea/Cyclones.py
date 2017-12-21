import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')
df1=pd.read_csv("/Users/gautam/Downloads/freq_cyclone-dep_bob_D-CS-SCS_1891-2015.csv")
df2=pd.read_csv("/Users/gautam/Downloads/freq_cyclone-dep_as_D-CS-SCS_1891-2015.csv")
df1=df1[df1['Annual']!=1189]
df2=df2[df2['Annual']!=216]
fig = plt.figure()
ax = fig.add_subplot(111)
BoB = plt.plot(df1['Annual'], 'green', label = 'Bay Of Bengal')
As = plt.plot(df2['Annual'], 'red', label = 'Arabian Sea')
plt.gca().axis([0, 125, -5, 20])
plt.gca().set_aspect('equal')
plt.xlabel('Year')
plt.ylabel('Number Of Cyclones')
plt.legend(frameon = False)
plt.xticks(range(0, len(df1['Year']), 20), ('1891', '1911', '1931', '1951', '1971', '1991', '2011'))
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
plt.axhline(y = 0, color = 'grey', alpha = 0.2, linestyle='--')
plt.axhline(y = 5, color = 'grey', alpha = 0.2, linestyle='--')
plt.axhline(y = 10, color = 'grey', alpha = 0.2, linestyle='--')
plt.axhline(y = 15, color = 'grey', alpha = 0.2, linestyle='--')
plt.axhline(y = 20, color = 'grey', alpha = 0.2, linestyle='--')
