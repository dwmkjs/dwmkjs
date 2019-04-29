 # pip install numpy

import statistics  as st
import numpy as np

input_x=[]
input_y=[]
n=input("enter number of elements:")
for i in range(0,n):
	input_x.append(input("enter x:"))
	input_y.append(input("enter y:"))
x=np.array(input_x, dtype =np.float64)
y=np.array(input_y, dtype =np.float64)
xy=[]
x_square=[]
x_mean=st.mean(x)
y_mean=st.mean(y)
xy_mean=st.mean(x*y)
x_square_mean=st.mean(x**2)
best_m=(x_mean*y_mean - xy_mean)/(x_mean**2-x_square_mean)
best_c=y_mean-x_mean*best_m
predict_x=input("enter x for prediction:");
predict_y=best_m*predict_x+best_c
print predict_y

# Output:

# comp@comp-ThinkCentre-M720t:~/Desktop$ python linear.py
# enter number of elements:5
# enter x:1
# enter y:5
# enter x:2
# enter y:4
# enter x:3
# enter y:6
# enter x:4
# enter y:5
# enter x:5
# enter y:6
# enter x for prediction:1
# 4.600000000000002
