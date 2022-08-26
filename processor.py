'''
Plots data to graphs. Takes input of 'all' or 'one'
'''

import sys
import matplotlib.pyplot as plt

#constants
ranks = ['', 'Iron', 'Bron', 'Silv', 'Gold', 'Plat', 'Diam', 'Mas+']

def createAllImages():
	#get the data
	inp = open('data-2.txt', 'r')
	lines = inp.readlines()

	#loop
	for line in lines:
		arr = line.split('\t')
		name = arr[0].split(" (")[0]
		point = []
		axis = []

		#data points
		for i in range(1, 8):
			point.append(float(arr[i]))
			axis.append(ranks[i])

		#decorate figure
		fig, ax = plt.subplots()
		ax.set(ylim=(44, 56))
		ax.set_ylabel('Winrate')
		ax.set_title(arr[0])
		ax.plot(axis, point, '-o')
		plt.savefig("plots/indiv/" + name + ".png")
		plt.close()

	#close files
	inp.close()

def createOneImage(champion):
	#get the data
	inp = open('data-2.txt', 'r')
	lines = inp.readlines()

	#loop
	for line in lines:
		arr = line.split('\t')
		name = arr[0].split(" (")[0]
		point = []
		axis = []

		if name == champion:
			#data points
			for i in range(1, 8):
				point.append(float(arr[i]))
				axis.append(ranks[i])

			#decorate figure
			fig, ax = plt.subplots()
			ax.set(ylim=(44, 56))
			ax.set_ylabel('Winrate')
			ax.set_title(arr[0])
			ax.plot(axis, point, '-o')
			plt.savefig("plots/" + name + ".png")
			break

	#close files
	inp.close()


if str(sys.argv[1]) == 'all':
	createAllImages()
elif str(sys.argv[1]) == 'one':
	createOneImage(sys.argv[2])


