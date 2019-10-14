import scipy.io
import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd

#dictionary format:
#['<subjectID>']: [sex, age, FSIQ, Neuroticism, Extraversion, Openness, Agreeableness, Conscientiousness]
def getData(path):
	files = [f for f in listdir(path+'/smallgraphs') if isfile(join(path+'/smallgraphs', f))]
	print(len(files))
	dictionary = {}

	xls = pd.ExcelFile(path+"/metainfo.xls")

	sheetX = xls.parse(0) #2 is the sheet number
	sheetX = xls.parse(0).values
	fileIndex = -1
	for row in sheetX:
		for i in range(len(files)):
			if files[i][:9] == row[0]:
				fileIndex = i

		data = scipy.io.loadmat(path+'/smallgraphs/'+files[fileIndex])
		a = data['fibergraph'].toarray()
		for i in range(70):
		    for j in range(i, 70):
		        a[j][i] = a[i][j]

		dictionary[row[0]] = [row[2], row[3], row[5], row[7], row[8], row[9], row[10], row[11], a]

	return dictionary


#example for how to get the data
dataDict = getData('/Users/cranme/Documents/CSE575/brainnetworks/')

for d in dataDict:
	print(dataDict[d][-1])