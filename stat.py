import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


f = open('studyRate.csv')
csv_f = csv.reader(f)

table = [[]]

for row in csv_f:
	if row[0] == "United States":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "United Kingdom":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Germany":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "France":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Switzerland":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Japan":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] =="Canada":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Denmark":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Netherlands":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)
	elif row[0] == "Finland":
		temp = []
		for i in range(1,10):
			temp.append(row[i])
		table.append(temp)

oX = []
oY = []
oZ = []

l = []
for i in range(11):
    l.append(i)
plt.yticks(l)

l = []
for i in range(9):
    l.append(i)
plt.xticks(l)

for i in range(len(table)):
	for j in range(len(table[i])):
		oX.append(j)
		oY.append(i)
		oZ.append(int(table[i][j]))

c = []
c.append('blue')
c.append('green')
c.append('red')
c.append('cyan')
c.append('purple')
c.append('yellow')
c.append('black')
c.append('blue')
c.append('green')
c.append('red')
c.append('cyan')
c.append('purple')
c.append('yellow')

colours = [c[item] for item in oY]


# ax.scatter(oX, oY, oZ, c=colours)

for n in range(10):
    x = []
    y = []
    for i in range(9):
        y.append(oZ[n*9+i])
        x.append(i)
    a, b = np.polyfit(x,y,1)
    ax.plot([0,9],[n,n],[b,a*10+b])


labels = [0]*11
labels[9] = "USA"
labels[8] = "UK"
labels[4] = "Germany"
labels[3] = "France"
labels[7] = "Switzerland"
labels[5] = "Japan"
labels[0] = "Canada"
labels[1] = "Denmark"
labels[6] = "Netherlands"
labels[2] = "Finland"
ax.set_yticklabels(labels)

labels = [0]*11
labels[0] = 2000
labels[1] = 2005
labels[2] = 2006
labels[3] = 2007
labels[4] = 2008
labels[5] = 2009
labels[6] = 2010
labels[7] = 2011
labels[8] = 2012
ax.set_xticklabels(labels)

plt.show()


  	