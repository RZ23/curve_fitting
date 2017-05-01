# import relative library
import numpy as np
from scipy.optimize import leastsq
import scipy.optimize as opt
import scipy
import pandas as pd
import math
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
import math
from tkinter.filedialog import askopenfilename

# get data from Excel files

dataName = askopenfilename()


#df = pd.read_excel(open("Pei's Project.xlsx",'rb'),sheetname = 'test2')
#df = pd.read_excel(open("Pei's Project.xlsx",'rb'),sheetname = 'test2')
#df = pd.read_excel(open("Pei's Project.xlsx",'rb'),sheetname = 'datasource')
df = pd.read_excel(open(dataName,'rb'),sheetname = 'Sheet1')
df = df[df.Z!=0]
# Transfer dataframe into tuple
subset = df[['X','Y','Z']]
dt_tup = [tuple(x) for x in subset.values]
# Transfer tuple to np.array type
ar = np.array(dt_tup)
###define the functions (equations) ###
def func(dt,a,b,c,x0,z0):
    # get x & y from array dt
    x = dt[:,0]
    y = dt[:,1]
    # return the z value
    #return z0+a*x+b*((x+x0)**2+y**2)+c*((x+x0)**2+y**2)**2
    #return z0+a*x+b*(1-np.sqrt(1-c*((x+ x0)**2 + y**2)))
    return z0+a*x+b*(1-np.sqrt(1-(c*((x*0.995446+ x0)**2+ y**2))))
# set start parameters

a = -0.0958
b = 30000
c = 3.47e-9
z0 = -44
x0 = 918
p0 = (a,b,c,x0,z0)

# copy the original parameters for compare
orig = p0
# set guess parameter (same as start parameters)
#guess = (0.825,5.2e-5,4.5e-14,918,0)
guess = (-0.0958,30000,3.47e-9,918,-44)
# main function, fitting the curve
params,pcov = opt.curve_fit(func,ar[:,:2],ar[:,2],guess,maxfev = 100000)
# get result (fitted parameters)
# print the result
#print("Based on the datasource",dataName," and sheet name: ",sheetName)
print("Based on the datasource",dataName)
print("a = ",params[0]," original a = ",orig[0])
print("b = ",params[1]," original b = ",orig[1])
print("c = ",params[2]," original c = ",orig[2])
print("X0 = ",params[3]," original X0 = ",orig[3])
print("Z0 = ",params[4]," original Z0 = ",orig[4])
# calculate the z-value based on the result
a = params[0]
b = params[1]
c= params[2]
x0 = params[3]
z0 = params[4]
#cz = z0+a*df['X']+b*((df['X']+x0)**2+df['Y']**2)+c*((df['X']+x0)**2+df['Y']**2)**2
#cz = z0+a*df['X']+b*(1-np.sqrt(1-c*((df['X']+ x0)**2 + df['Y']**2)))
cz = z0 + a*df['X']+ b*(1-np.sqrt(1-c*((df['X']*0.995446+ x0)**2+ df['Y']**2)))
res = cz - df['Z']
# save the result to Excel file
# Excel name: output_tuplmfit
# Sheet: Sheet1
df['cz'] = cz
df['res'] = res
#writer = pd.ExcelWriter('output_tuplmfit.xlsx', engine='xlsxwriter')
#df.to_excel(writer,'Sheet1')
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
df.to_excel(writer,"Sheet1")
#df.to_excel(writer,'datasource56')
#df.to_excel(writer,'datasource41')
writer.save()


