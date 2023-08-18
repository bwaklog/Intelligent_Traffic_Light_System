# -*- coding: utf-8 -*-
"""ugss.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_L_xmIu4dy7raOmUvFG8y969VOD1-IQT
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime
# %matplotlib inline



# import serial
# arduino = serial.Serial("/dev/cu.usbmodem1101", timeout = 1)
# arduino.readline()
# inp = int(arduino.readline().rstrip()) for input
# for output: just replace print by:
# arduino.write(bytes(x, 'utf-8')) where x is the output





while True:
  now = datetime.datetime.now()
  current_time = now.strftime("%H.00")
  i=int(input("enter junction: "))

  # 1 AND 3 LANE
  if i==1 or i==3:
    df = pd.read_csv('13_traffic_new.csv')
    X = df.iloc[:, :2].values
    y = df.iloc[:, -2].values
    for i in range(len(X)):
      X[i][0] = X[i][0][10:]
      X[i][0] = X[i][0].replace(':', '.')
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)  
    df = df.replace(r'^\s*$', np.nan, regex=True)
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X, y)
    regressor.predict([[current_time,1]])
    out = regressor.predict([[12.00,2]])
    import math
    out = math.ceil(float(out[0]))
    if(out < 10): print(0)
    elif(out >= 10 and out < 30): print(1)
    elif out >= 30 : print(2)



  # 2 AND 4 LANE
  else:
    daf = pd.read_csv('24_traffic.csv')
    X = daf.iloc[:, :2].values
    y = daf.iloc[:, -2].values
    for i in range(len(X)):
      X[i][0] = X[i][0][10:]
      X[i][0] = X[i][0].replace(':', '.')
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    daf = daf.replace(r'^\s*$', np.nan, regex=True)
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X, y) 
    out = regressor.predict([[current_time,2]])
    import math
    out = math.ceil(float(out[0]))
    if(out < 10): print(0)
    elif(out >= 10 and out < 30): print(1)
    elif out >= 30 : print(2)