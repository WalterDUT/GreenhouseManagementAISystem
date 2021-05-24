import pymongo

client = pymongo.MongoClient("localhost", 27017) #kết nối mongo
db = client['wateringSystem']  # Select the database
full_data = db.waterData
predict_data = db.predict
def addNewDataForStorage(id, nhietdo, doamdat, cuongdosang, doamkhongkhi):
    full_data.insert_one(
        {
            "_id": id,
            "temperature": nhietdo,
            "soil_moisture": doamdat,
            "light_intensity": cuongdosang,
            "air_humidity": doamkhongkhi,
        }
    )
def addNewDataJson(jsondata):
    full_data.insert_one(jsondata)
x={
    "air_humidity": "80",
    "light_intensity": "70",
    "soil_moisture": "67",
    "temperature": "29",
    "time": "8:00,15-2-2021"
}
# a=addNewDataJson(x)
# doc={}
# for i in range(10):
#     addNewDataForStorage(i,i+0.5,i+0.77,i+10,i+100)
# getHistoyData():
# data = db['waterData'].count_documents()
# data = full_data.find()
# a={'a':1,'b':2}
# jsondata={'id':1,a}
data = full_data.find()
jsondata = {}
i=0
for index in data:
    jsondata[i] = str(index)
    i+=1
print(jsondata)
# print(a)
# print(data.count())