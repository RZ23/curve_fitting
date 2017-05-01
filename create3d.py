from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from tkinter.filedialog import askopenfilename
import pandas as pd
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
dataName = askopenfilename()
df = pd.read_excel(open(dataName,'rb'),sheetname = 'Sheet1')
df = df[df.Z!=0]
# Make data.

X = df['X']
Y = df['Y']
Z = df['res']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_trisurf(X, Y, Z)
ax.scatter(X, Y, Z, c = 'b', marker = '.')
plt.show()
