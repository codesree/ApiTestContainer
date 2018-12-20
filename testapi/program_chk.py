from pymongo import MongoClient


print("Hello World!!")
# db = MongoClient('mongodb://prbk-pa001sap4v:27017')
db = MongoClient()

con = db['ApiTestContainer']
# col = con['homecontent_items']
# reqjson = col.find_one({"itemType": "HomeContent"})
# del reqjson['_id']
# print(reqjson)

#  --------- MODEL COPY -----------
# from mongoengine import *
# from django.contrib.auth.models import User
#
# class tag_check(models.Model):
#     #jsonreq = models.CharField(widget=forms.Textarea)
#     tag_id = models.CharField(max_length=234,unique=True)
#
#     def __str__(self):
#         return self.tag_id
#
#
# class Userpro(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.user.username
#


col = con['homecontent_item_draft']
# col.update(
#     {"itemType":"HomeContent"},
#     {"$set":{"draft":reqjson}}
#     )
rkey = "Alarm"
factnum = "testfact"
col.update({'draft.itemProperties.name': "" + rkey + ""},
                             {'$set': {
                                   'draft.itemProperties.$.value': factnum
                               }
                               })

checkjson = col.find_one({"itemType":"HomeContent"})
print(checkjson['draft'])

