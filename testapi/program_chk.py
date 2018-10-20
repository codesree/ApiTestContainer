from pymongo import MongoClient
import requests


# db = MongoClient('mongodb://ds117423.mlab.com:17423',
#                        username='srekanth',
#                        password='liberty@123',
#                        authSource='liberty_sti',
#                        authMechanism='SCRAM-SHA-1')

db = MongoClient('mongodb://prbk-pa001sap4v:27017')

con = db['api_test_container']

print(con)

col = con['asset_api']

col.insert({"name":"test_payload"})


    # asset_item = col.find_one({"itemType":"PersonalLiability"})
    #
    # del asset_item['_id']



    # print(asset_item)

    # loader("building_asset",asset_item)



# print(db.list_database_names())
# collect = "vehicle_item"
# col = con[collect]
#
# print(con.list_collection_names())
#
#
#
# asset_item = col.find_one({"itemType":"Vehicle"})
#
# print(asset_item)

#asset_item = asset_item





