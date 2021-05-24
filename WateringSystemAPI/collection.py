from pymongo import MongoClient

# from bson import ObjectId

client = MongoClient("mongodb://localhost:27017")  # host uri
db = client.wateringSystem  # Select the database
full_data = db.waterData
predict_data = db.predict


def addNewDataForStorage(time, nhietdo, doamdat, cuongdosang, doamkhongkhi):
    full_data.insert_one(
        {
            "time": time,
            "temperature": nhietdo,
            "soil_moisture": doamdat,
            "light_intensity": cuongdosang,
            "air_humidity": doamkhongkhi,
        }
    )


def addNewDataJson(jsondata):
    full_data.insert_one(jsondata)


def addManyDataJson(jsondatas):
    full_data.insert_many(jsondatas)


def getHistoyData():
    data = full_data.find()
    jsondata = {}
    i=0
    for index in data:
        jsondata[i] = str(index)
        i+=1
    return jsondata


def addNewDataPredicted(prediction, soil_moisture, upload_time):
    predict_data.insert(
        {
            "prediction": prediction,
            "soil_moisture": soil_moisture,
            "upload_time": upload_time,
        }
    )

