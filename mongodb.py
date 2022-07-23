import pymongo


client = pymongo.MongoClient("mongodb+srv://Dkumar37:Mongodb123@cluster0.grvwx.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print (db)

d = {
    "name":"Dilip",
    "email" : "Dilip@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

