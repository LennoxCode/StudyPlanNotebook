import matplotlib.pyplot as plt
import json
import os
import sys

import numpy as np
dictionary = json.load(open(os.path.join(sys.path[0],"file.json")))
xAxis = [key for key, value in dictionary.items()]
yAxis = [value for key, value in dictionary.items()]
plt.grid(True)

## LINE GRAPH ##
plt.plot(xAxis,yAxis, color='maroon', marker='o')
plt.xlabel('variable')
plt.ylabel('value')

## BAR GRAPH ##
fig = plt.figure()
plt.bar(xAxis,yAxis, color='maroon')
plt.xlabel('variable')
plt.ylabel('value')

plt.show()
