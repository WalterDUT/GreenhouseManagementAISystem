from flask import Flask
import pickle
# from modules.api.routes import mod

app = Flask(__name__)
print("accessing server .... please wait this might take a while")
filename='C:/Users/ADMIN/Desktop/PycharmProjects/FlaskApps/WateringSystemAPI/finalized_model.sav'
loaded_model = pickle.load(open(filename, "rb"))
import routes