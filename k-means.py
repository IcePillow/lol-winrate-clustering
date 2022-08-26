'''
Implements k-means alg on data-3.txt
Color palette from: https://www.heavy.ai/blog/12-color-palettes-for-telling-better-stories-with-your-data
'''

import random
from math import sqrt
from math import floor
import matplotlib.pyplot as plt

#constants
DIMS = 6
NUM_CENT = 15
LOOPS = 20
RANKS = ['Iron', 'Bron', 'Silv', 'Gold', 'Plat', 'Diam', 'Mas+']
RK_CG = ['IrBr', 'BrSi', 'SiGo', 'GoPl', 'PlDi', 'DiM+']
COLORS = ['#e60049', '#0bb4ff', '#50e991', '#e6d800', '#9b19f5', '#ffa300', '#dc0ab4', '#b3d4ff', '#00bfa0']

#fields
data = {}
centers = []
tags = {}  #dict of champion -> center idx

#load in the data
def loadData():
	inp = open('data-3.txt', 'r')
	line = inp.readline()
	while line:
		arr = line.split('\t')
		data[arr[0]] = (float(arr[1]),float(arr[2]),float(arr[3]),float(arr[4]),float(arr[5]),float(arr[6]))
		line = inp.readline()
	inp.close

#create the initial centers
def createCenters(amount):
	for i in range(amount):
		arr = []
		for j in range(DIMS):
			arr.append(random.uniform(-1.5, 1.5))
		centers.append(arr)

#calculates distance between the two vectors
def distance(vecOne, vecTwo):
	tot = 0
	for i in range(len(vecOne)):
		tot += (vecOne[i]-vecTwo[i])**2

	return sqrt(tot)

#assigns tags based on centers
def stepAssign():
	for i in data:
		dst = 100
		idx = -1
		for j in range(len(centers)):
			d = distance(data[i], centers[j])
			if d < dst:
				idx = j
				dst = d
		tags[i] = idx

#update the center positions
def stepUpdate():
	for i in range(len(centers)):
		centers[i] = [0]*DIMS
		ct = 0
		#add up all the values
		for j in data:
			if tags[j]==i:
				for k in range(DIMS):
					centers[i][k] += data[j][k]
				ct += 1
		#divide through
		if ct > 0:
			for j in range(DIMS):
				centers[i][j] = centers[i][j] / ct

#plots the clusterings of the differences
def plotDifClusters():
	for i in range(len(centers)):
		for j in range(len(centers[i])):
			c = centers[i][j]
			lab = c.split(' (')[0]
			mark = 'o'
			if floor(j/len(COLORS)) == 1:
				mark = '^'
			elif floor(j/len(COLORS)) == 1:
				mark = 'x'
			plt.plot(RK_CG, data[c], marker=mark, markersize=4, color=COLORS[j%len(COLORS)], label=lab)

		plt.legend(loc=2, prop={'size': 6})
		plt.ylabel('Winrate')
		plt.ylim([-2.5, 2.5])
		plt.savefig('plots/dif-cluster/cluster-' + str(i) + '.png')
		plt.close()

#Plots the clusterings from the differences with the absolute values
def plotAbsClusters():
	#load the abs data
	dat = {}
	with open('data-2.txt', 'r') as file:
		line = file.readline()
		while line:
			arr = line.split('\t')
			dat[arr[0]] = []

			for i in range(1, len(arr)):
				dat[arr[0]].append(float(arr[i]))

			line = file.readline()

	#plot the data
	for i in range(len(centers)):
		for j in range(len(centers[i])):
			c = centers[i][j]
			lab = c.split(' (')[0]
			mark = 'o'
			if floor(j/len(COLORS)) == 1:
				mark = '^'
			elif floor(j/len(COLORS)) == 1:
				mark = 'x'
			plt.plot(RANKS, dat[c], marker=mark, markersize=4, color=COLORS[j%len(COLORS)], label=lab)

		plt.legend(loc=2, prop={'size': 6})
		plt.ylabel('Winrate')
		plt.ylim([44, 56])
		plt.savefig('plots/abs-cluster/cluster-' + str(i) + '.png')
		plt.close()


#prepare
loadData()
#perform alg
createCenters(NUM_CENT)
for i in range(LOOPS):
	stepAssign()
	stepUpdate()
#group champs by center
for i in range(len(centers)):
	centers[i] = []
	for j in data:
		if i==tags[j]:
			centers[i].append(j)

plotDifClusters()
plotAbsClusters()
