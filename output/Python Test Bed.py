x = np.linspace(-1, .1, 50)

#WORKING
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('KNN_adult_reg.csv')
ax = df.loc[df['param_KNN__metric'] == 'manhattan'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="r", label='Manhattan Uniform')
df.loc[df['param_KNN__metric'] == 'manhattan'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="g", label='Manhattan Distance', ax=ax)
df.loc[df['param_KNN__metric'] == 'euclidean'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="purple", label='Euclidean Uniform', ax=ax)
df.loc[df['param_KNN__metric'] == 'euclidean'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="b", label='Euclidean Distance', ax=ax)
df.loc[df['param_KNN__metric'] == 'chebyshev'].loc[df['param_KNN__weights'] == 'uniform'].plot(kind="scatter", x=5,y=21, color="orange", label='Chebyshev Uniform', ax=ax)
df.loc[df['param_KNN__metric'] == 'chebyshev'].loc[df['param_KNN__weights'] == 'distance'].plot(kind="scatter", x=5,y=21, color="yellow", label='Chebyshev Distance', ax=ax)
ax.set_xlabel("# of Neighbors")
ax.set_ylabel("Accuracy")
ax.set_title("KNN Adult Train Accuracy")
plt.show()

######
# 3D attempt - WORKING
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SVM_RBF_madelon_reg.csv')
# print(df)

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

for c, m in [('r', 'o')]:
# [:,4] to access column 4
    xs = df.to_numpy()[:,4]
    ys = df.to_numpy()[:,5]
    zs = df.to_numpy()[:,13]
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('Alpha')
ax.set_ylabel('Gamma Frac')
ax.set_zlabel('Accuracy')
ax.set_title("SVM Madelon Test Accuracy")

plt.show()

# WORKING
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 1, 50)
df = pd.read_csv('DT_adult_timing.csv')
dg = pd.read_csv('ANN_adult_timing.csv')
dh = pd.read_csv('Boost_adult_timing.csv')
di = pd.read_csv('KNN_adult_timing.csv')
dj = pd.read_csv('SVM_RBF_adult_timing.csv')

ax = df.plot(x=0,y=2, color="b", label="DT")
dg.plot(x=0,y=2, color="g", label="ANN", ax=ax)
dh.plot(x=0,y=2, color="r", label="Boost", ax=ax)
di.plot(x=0,y=2, color="orange", label="KNN", ax=ax)
dj.plot(x=0,y=2, color="purple", label="SVM", ax=ax)

ax.set_xlabel("Percentage data included in Test Split")
ax.set_ylabel("Time (seconds)")
ax.set_title("Adult Testing Time")
plt.show()

