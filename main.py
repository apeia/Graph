import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

columns = ['Disease','County','Year','Sex','Cases','Population','Rate']

data = pd.read_csv("disease.csv", usecols=columns, delimiter=",")

def Cases(x,y):
  return [data.loc[x+2:y:3,'Cases'], data.loc[x+1:y:3,'Cases'], data.loc[x:y:3,'Cases']]




x = 116645
y = 120008

Mean = [Cases(x,y)[0].mean(), Cases(x,y)[1].mean(), Cases(x,y)[2].mean()]

fig = plt.figure(1) 

plt.bar('Male', Mean[0], color = 'r', width = .5)
plt.bar('Female', Mean[1], color = 'b', width = .5)
plt.bar('Total', Mean[2], color = 'g', width = .5)
plt.ylabel("Avg. Num. Cases/Year")

plt.legend(labels=['Male','Female','Total'], loc = 'upper left')


plt.title('Salmonellosis Graph')


fig2 = plt.figure(2)

x = 116930
y = 116987

dates = data.loc[x-1:y-3:3,'Year']


X = np.arange(len(dates))

plt.bar(X-.25, Cases(x,y)[0], color = 'r', width = .25)
plt.bar(X, Cases(x,y)[1], color = 'b', width = .25)
plt.bar(X+.25, Cases(x,y)[2][0:19], color = 'g', width = .25)

plt.legend(labels=['Male','Female','Total'], loc = 'upper right')

plt.xticks(rotation=60,ticks = [i for i in range(len(dates))], labels = dates)

plt.title('Salmonellosis per Year Graph (California County)')

fig3 = plt.figure(3)

x = 116645
y = 120008

dates = data.loc[x-1:y-3:3,'Year']


X = np.arange(len(dates))

plt.bar('Male', Cases(x,y)[0].sum(), color = 'r', width = .5)
plt.bar('Female', Cases(x,y)[1].sum(), color = 'b', width = .5)
plt.bar('Total', Cases(x,y)[2].sum(), color = 'g', width = .5)

plt.legend(labels=['Male','Female','Total'], loc = 'upper right')



plt.title('Total Salmonellosis Cases')


fig4 = plt.figure(4)

x = 116930
y = 116987

dates = data.loc[x-1:y-3:3,'Year']


X = np.arange(len(dates))

a = np.array(Cases(x,y)[0])
b = np.array(Cases(x,y)[1])

plt.bar(X-.125, a.cumsum(), color = 'r', width = .25)
plt.bar(X+.125, b.cumsum(), color = 'b', width = .25)


plt.legend(labels=['Male','Female'], loc = 'upper left')

plt.xticks(rotation=60,ticks = [i for i in range(len(dates))], labels = dates)

plt.title('Total Salmonellosis Cases per Year(California County)')
plt.show()




