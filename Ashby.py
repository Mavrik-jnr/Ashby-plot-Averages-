import pandas as pd
import numpy as np

# Materials Data
data = pd.read_csv('yes.csv')

# setting up identifiers
yes = data.keys()
yes = list(yes)
del yes[0]

identifiers = ['A', 'B', 'C', 'D', 'E', 'F']
for b in range(0,6):
    for a in yes:
        globals()[identifiers[b]] = yes[b]
        
features = [A,B, C,D,E,F]
keys = {'A':A, 'B':B, 'C':C, 'D':D, 'E':E, 'F':F}

#User interface 
print ('Available features are:')
for a in range(0,6):
    print (f'{identifiers[a]} : {features[a]}')
    
#User inputs
X = input('Welcome, please select from the alphabets the X feature you want on the ashby plot:  \n')
X = keys[X]
Y = input('Then select from the alphabets the Y feature you want on the ashby plot:  \n')
Y = keys[Y]
Z = float( input(F"what's your slope (performance index/guideline) between {X} and {Y}! (decimal or integer only | ex:3.0, 4.0, 3.5): " ) )
C = int( input(f"what's your intercept (realistic maximum possible for {Y})!: " ) )

#User_Data transformations (LOG SCALE BASE 10)
X = np.log10(data[X])
Y = np.log10(data[Y])
C = Y.max() + C
Z = float.as_integer_ratio(Z)
M = Z[0]
c = Z[1]

#Ranking function (in order of minimum vectorial positions of materials to the line equation)
def distance(X,Y):
    dist = (np.abs(-(c*M)*X + (c*Y) - (c*C) ) ) / np.sqrt(M**2+1**2)
    return dist
#distance transformation on datapoints
distan = distance(X,Y)
#appending distance to data
data['distance']=distan


#if you want to visualise it: data.sort_values(by=['test'])

#exporting in Csv
inp = input("please give a name to your new document:\n")
data.to_csv(f"{inp}.csv")
print ('Save Completed!, please check the file or directory this script is located for your file')

