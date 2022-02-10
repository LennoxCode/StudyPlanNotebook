# importing the required module
import matplotlib.pyplot as plt
import os
import sys
from matplotlib.style import available
import numpy as np
import json
json = json.load(open(os.path.join(sys.path[0],"publicData.json")))
solution = json["solution"]
##font = {'family' : 'normal',
##        'weight' : 'normal',
##        'size'   : 15}

##plt.rc('font', **font)
xAxis = [key for key, value in solution.items()]
yAxis = [len(value) for key, value in solution.items()]
N = 6
ind = np.arange(N)
width = 0.3
availablePlaces = [value for key, value in json["availablePlaces"].items()]
print(availablePlaces)
## BAR GRAPH ##
plt.figure(figsize=(15,10))
plt.bar(ind, availablePlaces , width, label='available Places')
plt.bar(ind + width, yAxis, width, label='assigned students')
plt.xlabel('Courses')
plt.ylabel('amount')
plt.title('available places in relation to students')
plt.xticks(ind + width / 2,xAxis)
plt.legend(loc='best')
## plt.bar(xAxis,yAxis, color='maroon')
## plt.title("Alle Kurse")
## plt.xlabel('Code')
## plt.ylabel('Zugelasse Studenten')

xAxis = [1, 2 , 3 , 4 , 5, 6]
yAxis = [0, 0 , 0 , 0 , 0, 0]
for code, students in solution.items():
  xAxis = [1, 2 , 3 , 4 , 5, 6]
  yAxis = [0, 0 , 0 , 0 , 0, 0]
  for student in students:
    yAxis[student["priority"] - 1] += 1
  fig = plt.figure()
  plt.title(code)
  plt.bar(xAxis,yAxis, color='maroon')
  plt.xlabel('prio')
  plt.ylabel('studis mit prio')
plt.show()