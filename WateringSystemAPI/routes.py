import os
import numpy as np
from app import app, loaded_model
from flask import Flask, request, jsonify
import collection as db
import preprocessing


@app.route("/")
def home():
    return "Welcome to water system of my dev team. Never do something stupid, if i know i will put my dick in ur ass"


@app.route("/storage", methods=["POST"])
def storage():
    data = request.values
    # print(jsonify(data))
    # ,data['light_intensity']
    db.addNewDataForStorage(data['time'],data['temperature'],data['soil_moisture'],data['air_humidity'])
    return jsonify(data)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.values
    if float(data["soil_moisture"]) < 0:
        response = {"prediction": -1}
        prediction=-1
        db.addNewDataPredicted(
            prediction=-1,
            soil_moisture=float(data["soil_moisture"]),
            upload_time=data["upload_time"],
        )
        # return jsonify(response)
        return str(prediction)
    x = preprocessing.convertDataShape(data["soil_moisture"])
    predictdata = loaded_model.predict(x)
    response = {"prediction": predictdata[0]}
    db.addNewDataPredicted(
        prediction=predictdata[0],
        soil_moisture=float(data["soil_moisture"]),
        upload_time=data["upload_time"],
    )
    # return jsonify(response)
    return str(predictdata[0])


@app.route("/getdata", methods=["GET"])
def getdata():
    data = db.getHistoyData()
    return jsonify(data)
