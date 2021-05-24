import pickle
import numpy as np

filename='C:/Users/ADMIN/Desktop/PycharmProjects/FlaskApps/WateringSystemAPI/finalized_model.sav'
loaded_model = pickle.load(open(filename, "rb"))
data=np.array([40])
datax=data.reshape(1,-1)
results=loaded_model.predict(datax)
print(results[0])