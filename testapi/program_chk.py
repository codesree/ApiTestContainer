from pymongo import MongoClient
from testpoc import testsome
import unittest

def testthis():
    suite = unittest.TestSuite()

    funcname = ["test_b_data"]

    for i in funcname:
        suite.addTest(testsome(i))

    tcrun = unittest.TextTestRunner()

    tcrun.run(suite)


if __name__ == '__main__':
    testthis()

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




