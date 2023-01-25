from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")
# Get the "csvjson" collection from the "test" database
db = client.test
collection = db.csv
# Open the JSON file and load the data
with open('csvjson.json', 'r') as file:
    data = json.load(file)
# Insert the data into the collection
collection.insert_many(data)
    
@app.route('/item', methods=['GET'])
def data():
    if request.method == 'GET':
        allData = db['csv'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            handle = data['Handle']
            title = data['Title']
            body = data['Body']
            vendor = data['Vendor']
            type = data['Type']
            tags = data['Tags']
            name1 = data['Option1 Name']
            value1 = data['Option1 Value']
            name2 = data['Option2 Name']
            value2 = data['Option2 Value']
            name3 = data['Option3 Name']
            value3 = data['Option3 Value']
            sku = data['Variant SKU']
            grams = data['Variant Grams']
            tracker = data['Variant Inventory Tracker']
            qty = data['Variant Inventory Qty']
            policy = data['Variant Inventory Policy']
            service = data['Variant Fulfillment Service']
            price = data['Variant Price']
            price = data['Variant Compare At Price']
            src = data['Image Src']
            dataDict = {
                'id': str(id),
                'handle': handle,
                'title': title,
                'body': body,
                'vendor': vendor,
                'type': type,
                'tags': tags,
                'name': name1,
                'value': value1,
                'name': name2,
                'value': value2,
                'name': name3,
                'value': value3,
                'sku': sku, 
                'grams': grams,
                'tracker': tracker,
                'qty': qty,
                'Policy': policy,
                'service': service,
                'price': price,
                'price': price,
                'src': src
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
    
@app.route('/items', methods=['GET'])
def get():    
       
    # GET all data from database
    if request.method == 'GET':
        allData = db['csv'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            title = data['Title']
            body = data['Body']
            sku = data['Variant SKU']
            dataDict = {
                'id': str(id),
                'title': title,
                'body': body,
                'sku': sku
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
    
@app.route('/users', methods=['POST'])
def post():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        handle = body['Handle']
        title = body['Title']
        body = body['Body']
        vendor = body['Vendor']
        type = body['Type']
        tags = body['Tags']
        name1 = body['Option1 Name']
        value1 = body['Option1 Value']
        name2 = body['Option2 Name']
        value2 = body['Option2 Value']
        name3 = body['Option3 Name']
        value3 = body['Option3 Value']
        sku = body['Variant SKU']
        grams = body['Variant Grams']
        tracker = body['Variant Inventory Tracker']
        qty = body['Variant Inventory Qty']
        policy = body['Variant Inventory Policy']
        service = body['Variant Fulfillment Service']
        price = body['Variant Price']
        price = body['Variant Compare At Price']
        src = body['Image Src']
        # db.users.insert_one({
        db['csv'].insert_many({
            "handle": handle,
            "title": title,
            "body": body,
            "vendor": vendor,
            "type": type,
            "tags": tags,
            "name": name1,
            "value": value1,
            "name": name2,
            "value": value2,
            "name": name3,
            "value": value3,
            "sku": sku, 
            "grams": grams,
            "tracker": tracker,
            "qty": qty,
            "Policy": policy,
            "service": service,
            "price": price,
            "price": price,
            "src": src
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            'handle': handle,
            'title': title,
            'body': body,
            'vendor': vendor,
            'type': type,
            'tags': tags,
            'name': name1,
            'value': value1,
            'name': name2,
            'value': value2,
            'name': name3,
            'value': value3,
            'sku': sku, 
            'grams': grams,
            'tracker': tracker,
            'qty': qty,
            'Policy': policy,
            'service': service,
            'price': price,
            'price': price,
            'src': src
        })
    
@app.route('/users/<string:id>', methods=['DELETE'])
def onedata(id):
    # DELETE a data
    if request.method == 'DELETE':
        db['csv'].delete_many({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is deleted!'})
    
if __name__ == '__main__':
    app.run(debug=True,port=8080)