import numpy as np
import os,datetime,json
import matplotlib.pyplt as plt



def pullHeartRateData(pathToFile,datetimeOffset=None):
	f = open(pathToFile)
	data = json.load(f)
	close(f)
	hr = np.array([v['value']['bpm'] for v in data])
	confidence = np.array([v['value']['confidence'] for v in data])
	datetime = np.array( [datetime.datetime.strptime(v['dateTime'],'%m/%d/%y %H:%M:%S') for v in data])
	if datetimeOffset is not None:
		datetime = datetime - datetimeOffset
	return hr, confidence, datetime

