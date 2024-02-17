import numpy as np
import os,datetime,json
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.dates as mdates

xformatter = mdates.DateFormatter('%H:%M')




def pullHeartRateData(pathToFile,datetimeOffset=None):
	f = open(pathToFile)
	data = json.load(f)
	f.close()
	hr = np.array([v['value']['bpm'] for v in data])
	confidence = np.array([v['value']['confidence'] for v in data])
	dt = np.array( [datetime.datetime.strptime(v['dateTime'],'%m/%d/%y %H:%M:%S') for v in data])
	if datetimeOffset is not None:
		dt = dt - datetimeOffset
	return hr, confidence, dt

def plotAllDays(directory,dt_offset=None):
	if dt_offset is None:
		dt_offset = datetime.timedelta(hours=0)
	if isinstance(dt_offset,int):
		dt_offset = datetime.timedelta(hours=dt_offset)
	files = os.listdir(directory)
	files = [f for f in files if 'heart' in f]
	figIx = 1
	allHr = []
	alldt = []
	for fileName in files:
		print(f'loading {fileName}')
		hr,confidence,dt = pullHeartRateData(os.path.join(directory,fileName),dt_offset)
		plt.figure(figIx)
		
		figIx=figIx+1
		ax= plt.subplot(111)

		ax.plot(dt,hr)
		ax.xaxis.set_major_formatter(xformatter)
		ax.set_title(f'Heart Rate for {dt[0].date()}')
		allHr.append(hr)
		alldt.append(dt)

	
	plt.figure(figIx)
	[plt.plot(alldt[ix],allHr[ix]) for ix in range(len(files))]
	plt.title('all data')
	plt.show()
def plotSingleDay(directory,dt_offset=None,annotationTimes=None,annotationLabels=None):
	pass