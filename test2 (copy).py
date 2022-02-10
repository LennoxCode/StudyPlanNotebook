
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
plt.show()

# importing the required module
import matplotlib.pyplot as plt
import os
import sys
from matplotlib.style import available
import numpy as np
import json
json = json.load(open(os.path.join(sys.path[0],"publicData.json")))
solution = json["solution"]
xAxis = [1, 2 , 3 , 4 , 5, 6]
yAxis = [0, 0 , 0 , 0 , 0, 0]
# Some example data to display
fig, ax = plt.subplots(3, 2, figsize=(15,10))
fig.suptitle('number of Wishes with Priority per course')
index = 0
for code, students in solution.items():
  xAxis = [1, 2 , 3 , 4 , 5, 6]
  yAxis = [0, 0 , 0 , 0 , 0, 0]
  for student in students:
    yAxis[student["priority"] - 1] += 1
  ax[index // 2][index % 2].bar(xAxis,yAxis, color='maroon')
  ax[index // 2][index % 2].title.set_text(code)
  index += 1
plt.show()

import matplotlib.pyplot as plt
import os
import sys
from matplotlib.style import available
import numpy as np
import json
json = json.load(open(os.path.join(sys.path[0],"publicData.json")))
solution = json["solution"]
courseWishes = json["courseWishes"]
sizes = [0, 0, 0, 0, 0]
for wish in courseWishes:
    wishedCourses = wish["maxCourses"]
    student = wish["user"]
    gotCourses = 0
    for code, students in solution.items():
        result = any(student == studentInCourse["user"] for studentInCourse in students)
        if(result): gotCourses +=1
    sizes[wishedCourses - gotCourses] += 1
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'All Courses', 'One Less', 'Two Less', 'Three Less', 'Difference Bigger Three'

explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots(figsize=(15,10))
wedges, texts, autotexts = ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=180)
ax1.legend(wedges, labels,
          title="course wish difference",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          prop={'size': 18})

plt.setp(autotexts, size=15, weight="normal")


# importing the required module
import matplotlib.pyplot as plt
import os
import sys
from matplotlib.style import available
import numpy as np
import json
json = json.load(open(os.path.join(sys.path[0],"publicData.json")))
solution = json["solution"]
courseWishes = json["courseWishes"]
##font = {'family' : 'normal',
##        'weight' : 'normal',
##        'size'   : 15}

##plt.rc('font', **font)
xAxis = [0, 1, 2, 3, 4, 5, 6]
yAxis = [0, 0, 0, 0, 0, 0, 0]
N = 6
ind = np.arange(N)
width = 0.7

## BAR GRAPH ##
for wish in courseWishes:
    yAxis[wish["maxCourses"]] += 1
plt.figure(figsize=(15,10))
plt.bar(xAxis, yAxis, width, label='assigned students')
plt.xlabel('course wish amount')
plt.ylabel('amount')
plt.title('available places in relation to students')
plt.legend(loc='best')
## plt.bar(xAxis,yAxis, color='maroon')
## plt.title("Alle Kurse")
## plt.xlabel('Code')
## plt.ylabel('Zugelasse Studenten')
plt.show()

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
