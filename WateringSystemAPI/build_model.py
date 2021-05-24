import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import MinMaxScaler

# import random
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Create data
def cthuc(x):
    ct = (
        +(13 * pow(x, 11) / 60908203125000)
        - (2231 * pow(x, 10) / 17718750000000)
        + (4733 * pow(x, 9) / 141750000000)
        - (124063 * pow(x, 8) / 23625000000)
        + (4283633 * pow(x, 7) / 7875000000)
        - (52572083 * pow(x, 6) / 1350000000)
        + (445647469 * pow(x, 5) / 226800000)
        - (1979721799 * pow(x, 4) / 28350000)
        + (97059281857 * pow(x, 3) / 56700000)
        - (1446184559 * pow(x, 2) / 52500)
        + (906835562 * x / 3465)
        - 1111264
    )
    return ct


def createData():
    values = []
    results = []
    for i in range(25, 100):
        if i <= 80:
            result = cthuc(i)
            result2 = cthuc(i + 0.5)
            values.append(i)
            values.append(i + 0.5)
            results.append(result)
            results.append(result2)
        else:
            values.append(i)
            values.append(i + 0.5)
            results.append(-1)
            results.append(-1)
        # print("t0:", i)
        # print("time:", result)
    data = np.array([values, results])
    data = data.T
    # print(data.shape)
    pf = pd.DataFrame(data, columns=["doam", "thoigiantuoi"])
    return pf


# preprocessing data
dataFrame = createData()
X = dataFrame.drop("thoigiantuoi", axis=1)
Y = dataFrame["thoigiantuoi"].values
maxX = X.max()
minX = X.min()
x = X.values
X_s = []
for i in x:
    X_s.append(1.0 * (float(i) - minX) / (maxX - minX))
# X_s = 1.0 * (float(x) - minX) / (maxX - minX)
# min_max_scaler = MinMaxScaler()
# X_scale = min_max_scaler.fit_transform(X)
# createData()
# X_back = []
# for i in range(len(X_s)):
#     X_back.append(X_s[i] * (maxX - minX) + minX)
# print(X_s[:3])
# print(X_scale[:3])
# print(X_back[:3])

X_train, X_val_test, Y_train, Y_val_test = train_test_split(X_s, Y, test_size=0.2)
# X_test,X_validation,Y_test,Y_validation=train_test_split(X_val_test,Y_val_test,test_size=0.5)
reg = GradientBoostingRegressor()
reg.fit(X_train, Y_train)

# print(Y)
# print(y_GBR)
# Y_back=[]
# y_GBR_b=[]
# for i in range(len(Y_val_test)):
#   Y_back.append(Y_val_test[i]*(maxY-minY)+minY)
#   y_GBR_b.append(y_GBR[i]*(maxY-minY)+minY)

# save the model to disk
filename = "C:/Users/ADMIN/Desktop/PycharmProjects/FlaskApps/WateringSystemAPI/modules/backend/finalized_model.sav"
pickle.dump(reg, open(filename, "wb"))

# load the model from disk
loaded_model = pickle.load(open(filename, "rb"))
# predict and plot results
y_GBR = loaded_model.predict(X_val_test)
plt.figure(figsize=(10, 5))
plt.plot(Y_val_test, "g-", label="actual data")
plt.plot(y_GBR, "r-", label="predicted data")
plt.title("LinearRegression")
plt.xlabel("Len(data)")
plt.ylabel("Price")
plt.legend(loc="best")
plt.show()
